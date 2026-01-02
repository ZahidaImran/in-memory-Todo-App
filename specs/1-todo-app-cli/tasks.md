---
description: "Task list for In-Memory Console Todo Application implementation"
---

# Tasks: In-Memory Console Todo Application

**Input**: Design documents from `/specs/1-todo-app-cli/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Note**: This implementation follows a layered architecture with CLI, Domain, and Storage layers as specified in the plan.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths follow the structure defined in plan.md

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan in src/todo_app/
- [X] T002 [P] Create pyproject.toml with project configuration and dependencies
- [X] T003 [P] Create directory structure: src/todo_app/{cli,domain,storage}, tests/{unit,integration}

---
## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Create Todo model in src/todo_app/domain/models.py with id, description, completed fields
- [X] T005 [P] Create in-memory storage implementation in src/todo_app/storage/memory_storage.py
- [X] T006 [P] Create domain services for business operations in src/todo_app/domain/services.py
- [X] T007 Create CLI argument parser in src/todo_app/cli/main.py
- [X] T008 Create application entry point in src/todo_app/__main__.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---
## Phase 3: User Story 1 - Add Todo Items (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new todo items to their list using the command line interface

**Independent Test**: Can be fully tested by running the add command and verifying the todo appears in the list, delivering the core value of adding items to a todo list.

### Implementation for User Story 1

- [X] T009 [P] [US1] Implement Todo validation rules in src/todo_app/domain/models.py
- [X] T010 [US1] Implement add_todo method in src/todo_app/domain/services.py
- [X] T011 [US1] Implement add command handler in src/todo_app/cli/main.py
- [X] T012 [US1] Connect add command to domain service in src/todo_app/__main__.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---
## Phase 4: User Story 2 - View Todo List (Priority: P1)

**Goal**: Allow users to see all their todo items in a formatted list

**Independent Test**: Can be fully tested by adding todos and then viewing the list, delivering the core value of seeing all todo items.

### Implementation for User Story 2

- [X] T013 [P] [US2] Implement get_all_todos method in src/todo_app/domain/services.py
- [X] T014 [US2] Implement list/view command handler in src/todo_app/cli/main.py
- [X] T015 [US2] Connect list command to domain service in src/todo_app/__main__.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---
## Phase 5: User Story 3 - Mark Todo as Complete (Priority: P2)

**Goal**: Enable users to mark a specific todo as complete to track their progress

**Independent Test**: Can be fully tested by adding a todo, marking it as complete, and viewing the list to confirm completion status, delivering the value of task tracking.

### Implementation for User Story 3

- [X] T016 [P] [US3] Implement complete_todo method in src/todo_app/domain/services.py
- [X] T017 [US3] Implement complete command handler in src/todo_app/cli/main.py
- [X] T018 [US3] Connect complete command to domain service in src/todo_app/__main__.py

**Checkpoint**: User Stories 1, 2, AND 3 should all work independently

---
## Phase 6: User Story 4 - Update Todo Description (Priority: P3)

**Goal**: Allow users to modify the description of an existing todo item

**Independent Test**: Can be fully tested by adding a todo, updating its description, and viewing the list to confirm the change, delivering the value of flexible task management.

### Implementation for User Story 4

- [X] T019 [P] [US4] Implement update_todo method in src/todo_app/domain/services.py
- [X] T020 [US4] Implement update command handler in src/todo_app/cli/main.py
- [X] T021 [US4] Connect update command to domain service in src/todo_app/__main__.py

**Checkpoint**: User Stories 1, 2, 3, AND 4 should all work independently

---
## Phase 7: User Story 5 - Delete Todo Items (Priority: P3)

**Goal**: Allow users to remove completed or unwanted todo items from their list

**Independent Test**: Can be fully tested by adding a todo, deleting it, and viewing the list to confirm its removal, delivering the value of list maintenance.

### Implementation for User Story 5

- [X] T022 [P] [US5] Implement delete_todo method in src/todo_app/domain/services.py
- [X] T023 [US5] Implement delete command handler in src/todo_app/cli/main.py
- [X] T024 [US5] Connect delete command to domain service in src/todo_app/__main__.py

**Checkpoint**: All user stories should now be independently functional

---
## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T025 [P] Add error handling for invalid index access in src/todo_app/domain/services.py
- [X] T026 [P] Add error handling for empty description validation in src/todo_app/domain/models.py
- [X] T027 [P] Add proper error messages for CLI commands in src/todo_app/cli/main.py
- [X] T028 [P] Create documentation in docs/quickstart.md
- [X] T029 Add proper formatting for todo display in src/todo_app/cli/main.py
- [X] T030 Run quickstart validation to ensure all commands work as expected

---
## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May depend on US1/US2 for testing but should be independently testable
- **User Story 4 (P3)**: Can start after Foundational (Phase 2) - May depend on US1 for testing but should be independently testable
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - May depend on US1 for testing but should be independently testable

### Within Each User Story

- Models before services
- Services before CLI handlers
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---
## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---
## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence