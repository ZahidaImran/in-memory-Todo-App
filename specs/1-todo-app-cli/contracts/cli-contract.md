# API Contract: Todo CLI Application

## Command Interface

### Add Todo
- **Command**: `add <description>`
- **Input**: String description of the todo
- **Output**: Confirmation message with todo ID
- **Errors**:
  - Empty description → Error message

### List Todos
- **Command**: `list` or `view`
- **Input**: None
- **Output**: Formatted list of all todos with index and completion status
- **Errors**: None

### Complete Todo
- **Command**: `complete <index>`
- **Input**: Integer index of the todo to complete
- **Output**: Confirmation message
- **Errors**:
  - Invalid index → Error message

### Update Todo
- **Command**: `update <index> <new_description>`
- **Input**: Integer index and new string description
- **Output**: Confirmation message
- **Errors**:
  - Invalid index → Error message
  - Empty description → Error message

### Delete Todo
- **Command**: `delete <index>`
- **Input**: Integer index of the todo to delete
- **Output**: Confirmation message
- **Errors**:
  - Invalid index → Error message