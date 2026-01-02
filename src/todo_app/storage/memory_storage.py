"""In-memory storage implementation for todo items."""

from typing import List, Optional
from ..domain.models import Todo


class MemoryStorage:
    """In-memory storage for todo items."""

    def __init__(self):
        """Initialize the storage with an empty list of todos."""
        self._todos: List[Todo] = []
        self._next_id = 1

    def add_todo(self, description: str) -> Todo:
        """Add a new todo to the storage."""
        todo = Todo(id=self._next_id, description=description, completed=False)
        self._todos.append(todo)
        self._next_id += 1
        return todo

    def get_all_todos(self) -> List[Todo]:
        """Get all todos from storage."""
        return self._todos.copy()

    def get_todo_by_index(self, index: int) -> Optional[Todo]:
        """Get a todo by its 0-based index."""
        if 0 <= index < len(self._todos):
            return self._todos[index]
        return None

    def update_todo(self, index: int, description: str) -> Optional[Todo]:
        """Update a todo's description by its 0-based index."""
        if 0 <= index < len(self._todos):
            self._todos[index] = Todo(
                id=self._todos[index].id,
                description=description,
                completed=self._todos[index].completed
            )
            return self._todos[index]
        return None

    def complete_todo(self, index: int) -> bool:
        """Mark a todo as complete by its 0-based index."""
        if 0 <= index < len(self._todos):
            self._todos[index].completed = True
            return True
        return False

    def delete_todo(self, index: int) -> bool:
        """Delete a todo by its 0-based index."""
        if 0 <= index < len(self._todos):
            self._todos.pop(index)
            return True
        return False

    def get_next_id(self) -> int:
        """Get the next available ID for a new todo."""
        return self._next_id