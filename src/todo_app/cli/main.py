"""CLI entry point and command routing with interactive mode."""

import sys
import re
from typing import List, Tuple, Optional
from ..domain.models import Todo
from ..domain.services import TodoService
from ..storage.memory_storage import MemoryStorage


def format_todo(todo: Todo, index: int) -> str:
    """Format a todo for display."""
    status = "✓" if todo.completed else "○"
    return f"[{status}] {index}. {todo.description}"


def parse_command(user_input: str) -> Tuple[str, List[str]]:
    """Parse user input into command and arguments."""
    parts = user_input.strip().split()
    if not parts:
        return "", []

    command = parts[0].lower()

    # Handle commands that may have quoted arguments
    if command in ["add", "update"] and '"' in user_input:
        # Use regex to handle quoted strings
        pattern = r'(\S+)|"([^"]*)"'
        matches = re.findall(pattern, user_input.strip())
        # Each match is a tuple (non-quoted, quoted), we take the non-empty one
        tokens = [match[0] if match[0] else match[1] for match in matches]
        if tokens:
            command = tokens[0].lower()
            args = tokens[1:] if len(tokens) > 1 else []
        else:
            command = ""
            args = []
    else:
        # Simple split for commands without quoted strings
        all_parts = user_input.strip().split()
        command = all_parts[0].lower() if all_parts else ""
        args = all_parts[1:] if len(all_parts) > 1 else []

    return command, args


def add_todo_interactive(description: str, service: TodoService) -> None:
    """Handle the add command interactively."""
    try:
        todo = service.add_todo(description)
        print(f"Added todo #{todo.id}: {todo.description}")
    except ValueError as e:
        print(f"Error: {e}")


def list_todos_interactive(service: TodoService) -> None:
    """Handle the list command interactively."""
    todos = service.get_all_todos()

    if not todos:
        print("No todos found.")
        return

    for i, todo in enumerate(todos, 1):
        print(format_todo(todo, i))


def complete_todo_interactive(index_str: str, service: TodoService) -> None:
    """Handle the complete command interactively."""
    try:
        index = int(index_str)
        success = service.complete_todo(index)
        if success:
            print(f"Marked todo #{index} as complete")
        else:
            print(f"Error: Could not complete todo #{index}")
    except ValueError:
        print(f"Error: Index must be a number")
    except IndexError as e:
        print(f"Error: {e}")


def update_todo_interactive(index_str: str, new_description: str, service: TodoService) -> None:
    """Handle the update command interactively."""
    try:
        index = int(index_str)
        success = service.update_todo(index, new_description)
        if success:
            print(f"Updated todo #{index}")
        else:
            print(f"Error: Could not update todo #{index}")
    except ValueError:
        print(f"Error: Index must be a number")
    except IndexError as e:
        print(f"Error: {e}")


def delete_todo_interactive(index_str: str, service: TodoService) -> None:
    """Handle the delete command interactively."""
    try:
        index = int(index_str)
        success = service.delete_todo(index)
        if success:
            print(f"Deleted todo #{index}")
        else:
            print(f"Error: Could not delete todo #{index}")
    except ValueError:
        print(f"Error: Index must be a number")
    except IndexError as e:
        print(f"Error: {e}")


def show_help() -> None:
    """Display help information."""
    help_text = """
Available commands:
  add "description"     - Add a new todo
  list / view          - Show all todos
  complete <index>     - Mark todo at index as complete
  update <index> "desc" - Update todo description at index
  delete <index>       - Delete todo at index
  help / ?             - Show this help
  exit / quit          - Exit the application
"""
    print(help_text)


def interactive_main() -> None:
    """Main interactive CLI loop."""
    storage = MemoryStorage()
    service = TodoService(storage)

    print("Todo App - Interactive Mode")
    print("Type 'help' for available commands or 'exit' to quit")
    print("-" * 50)

    while True:
        try:
            user_input = input("> ").strip()

            if not user_input:
                continue

            command, args = parse_command(user_input)

            if command in ['exit', 'quit']:
                print("Goodbye!")
                break
            elif command in ['help', '?']:
                show_help()
            elif command == 'add':
                if len(args) >= 1:
                    description = " ".join(args)
                    add_todo_interactive(description, service)
                else:
                    print("Error: add command requires a description")
            elif command in ['list', 'view']:
                if len(args) == 0:
                    list_todos_interactive(service)
                else:
                    print(f"Error: {command} command takes no arguments")
            elif command == 'complete':
                if len(args) == 1:
                    complete_todo_interactive(args[0], service)
                else:
                    print("Error: complete command requires an index")
            elif command == 'update':
                if len(args) >= 2:
                    index_str = args[0]
                    new_description = " ".join(args[1:])
                    update_todo_interactive(index_str, new_description, service)
                else:
                    print("Error: update command requires an index and new description")
            elif command == 'delete':
                if len(args) == 1:
                    delete_todo_interactive(args[0], service)
                else:
                    print("Error: delete command requires an index")
            else:
                print(f"Unknown command: {command}. Type 'help' for available commands.")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except EOFError:
            print("\nGoodbye!")
            break


def main() -> None:
    """Main CLI entry point - now supports interactive mode."""
    interactive_main()


if __name__ == "__main__":
    main()