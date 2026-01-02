"""Todo model and core business logic."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Todo:
    """Represents a todo item."""

    id: int
    description: str
    completed: bool = False

    def __post_init__(self):
        """Validate the todo after initialization."""
        if not self.description or not self.description.strip():
            raise ValueError("Description cannot be empty or contain only whitespace")

        if len(self.description) > 1000:
            raise ValueError("Description is too long (maximum 1000 characters)")

        if self.id <= 0:
            raise ValueError("ID must be a positive integer")


def validate_todo_description(description: str) -> None:
    """Validate a todo description according to business rules."""
    if not description or not description.strip():
        raise ValueError("Description cannot be empty or contain only whitespace")

    if len(description) > 1000:
        raise ValueError("Description is too long (maximum 1000 characters)")