# Quickstart Guide: Todo CLI Application

## Prerequisites
- Python 3.13 or higher
- UV package manager (optional, for dependency management)

## Installation
1. Clone the repository
2. Navigate to the project directory
3. (Optional) Create a virtual environment: `python -m venv venv && source venv/bin/activate`
4. Install dependencies: `uv sync` (or `pip install -e .`)

## Usage
Run the application using:
```bash
python -m src.todo_app
```

Or if installed as a package:
```bash
todo-app
```

## Available Commands
- `add "description"` - Add a new todo with the specified description
- `list` or `view` - Display all todos with their completion status
- `complete <index>` - Mark the todo at the specified index as complete
- `update <index> "new description"` - Update the description of the todo at the specified index
- `delete <index>` - Remove the todo at the specified index

## Examples
```bash
# Add a new todo
python -m src.todo_app add "Buy groceries"

# View all todos
python -m src.todo_app list

# Mark the first todo as complete
python -m src.todo_app complete 1

# Update a todo description
python -m src.todo_app update 1 "Buy groceries and cook dinner"

# Delete a todo
python -m src.todo_app delete 1
```

## Project Structure
- `src/todo_app/` - Main application source code
  - `cli/main.py` - Command-line interface and argument parsing
  - `domain/models.py` - Todo model and business logic
  - `domain/services.py` - Domain services for business operations
  - `storage/memory_storage.py` - In-memory storage implementation
- `tests/` - Unit and integration tests
- `docs/` - Documentation files