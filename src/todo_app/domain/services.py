"""Domain services for business operations."""

from typing import List, Optional
from .models import Todo, validate_todo_description
from ..storage.memory_storage import MemoryStorage


class TodoService:
    """Service class for business operations on todos."""

    def __init__(self, storage: MemoryStorage):
        """Initialize the service with a storage instance."""
        self.storage = storage

    def add_todo(self, description: str) -> Todo:
        """Add a new todo after validation."""
        validate_todo_description(description)
        return self.storage.add_todo(description)

    def get_all_todos(self) -> List[Todo]:
        """Get all todos."""
        return self.storage.get_all_todos()

    def complete_todo(self, index: int) -> bool:
        """Mark a todo as complete by index (1-based for user input)."""
        if index < 1:
            raise IndexError("Todo index must be 1 or greater")

        # Convert from 1-based user index to 0-based internal index
        internal_index = index - 1

        todo = self.storage.get_todo_by_index(internal_index)
        if todo is None:
            raise IndexError(f"Todo with index {index} does not exist")

        return self.storage.complete_todo(internal_index)

    def update_todo(self, index: int, new_description: str) -> bool:
        """Update a todo's description by index (1-based for user input)."""
        if index < 1:
            raise IndexError("Todo index must be 1 or greater")

        validate_todo_description(new_description)

        # Convert from 1-based user index to 0-based internal index
        internal_index = index - 1

        todo = self.storage.get_todo_by_index(internal_index)
        if todo is None:
            raise IndexError(f"Todo with index {index} does not exist")

        updated_todo = self.storage.update_todo(internal_index, new_description)
        return updated_todo is not None

    def delete_todo(self, index: int) -> bool:
        """Delete a todo by index (1-based for user input)."""
        if index < 1:
            raise IndexError("Todo index must be 1 or greater")

        # Convert from 1-based user index to 0-based internal index
        internal_index = index - 1

        todo = self.storage.get_todo_by_index(internal_index)
        if todo is None:
            raise IndexError(f"Todo with index {index} does not exist")

        return self.storage.delete_todo(internal_index)