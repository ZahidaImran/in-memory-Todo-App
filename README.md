# Todo CLI Application

A command-line todo application with in-memory storage, built as part of the Hackathon2-phase1 project. This application demonstrates spec-driven, agentic development workflows.

## Project Overview

This is a console-based todo application that allows users to manage their tasks through a command-line interface. The application stores todos in memory and provides basic CRUD operations for task management.

## Features

- **Add todos** - Add new todo items with descriptions
- **View/List todos** - Display all todos with their completion status
- **Mark todos as complete** - Update the completion status of specific todos
- **Update todos** - Modify the description of existing todos
- **Delete todos** - Remove specific todos from the list
- **Interactive mode** - Command-line interface for easy navigation

## Installation

1. Clone the repository
2. Ensure you have Python 3.13 or higher installed
3. Install the package using pip:

```bash
pip install .
```

Or run directly from the source:

```bash
python -m src.todo_app
```

## Usage

The application can be run in interactive mode where you can enter commands:

```bash
todo-app
```

### Available Commands

- `add "description"` - Add a new todo with the specified description
- `list` or `view` - Display all todos with their completion status
- `complete <index>` - Mark the todo at the specified index as complete
- `update <index> "new description"` - Update the description of the todo at the specified index
- `delete <index>` - Remove the todo at the specified index
- `help` or `?` - Show available commands
- `exit` or `quit` - Exit the application

### Example Session

```
> add "Buy groceries"
Added: Buy groceries
> add "Complete project"
Added: Complete project
> list
1. [ ] Buy groceries
2. [ ] Complete project
> complete 1
Marked as complete: Buy groceries
> list
1. [x] Buy groceries
2. [ ] Complete project
> exit
```

## Project Structure

- `src/todo_app/cli/main.py` - Main CLI logic and interactive mode
- `src/todo_app/domain/models.py` - Todo model definition
- `src/todo_app/domain/services.py` - Business logic services
- `src/todo_app/storage/memory_storage.py` - In-memory storage implementation
- `specs/1-todo-app-cli/` - Specification, plan, and tasks documentation

## Architecture

The application follows a clean, layered architecture:

1. **CLI Layer**: Handles user input and command parsing
2. **Domain Layer**: Contains models and business logic
3. **Storage Layer**: In-memory storage implementation

## Development

### Prerequisites

- Python 3.13 or higher

### Running Tests

The project includes test scripts:
- `simple_test.py` - Basic functionality tests
- `test_interactive.py` - Interactive testing script

## Contributing

We welcome contributions to this project. Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions about this project, please contact the maintainers.