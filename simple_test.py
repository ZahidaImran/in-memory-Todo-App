#!/usr/bin/env python3
"""Simple test to verify the interactive functionality."""

from src.todo_app.cli.main import interactive_main

def test_direct():
    """Test the interactive_main function directly."""
    print("Testing interactive functionality directly...")
    print("This will start the interactive mode. Type 'exit' to quit.")

    # This will run the interactive loop
    interactive_main()

if __name__ == "__main__":
    test_direct()