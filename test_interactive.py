#!/usr/bin/env python3
"""Test script to verify the interactive functionality of the todo app."""

import subprocess
import sys
import time
from threading import Thread
import queue

def test_interactive_mode():
    """Test the interactive mode of the todo app."""
    print("Testing interactive mode...")

    # Start the interactive app as a subprocess
    process = subprocess.Popen(
        [sys.executable, "-m", "src.todo_app"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        universal_newlines=True
    )

    # Send a series of commands to test the functionality
    commands = [
        "help\n",
        "add \"First todo item\"\n",
        "add \"Second todo item\"\n",
        "list\n",
        "complete 1\n",
        "list\n",
        "update 2 \"Updated second todo item\"\n",
        "list\n",
        "delete 1\n",
        "list\n",
        "exit\n"
    ]

    # Send commands to the process
    for cmd in commands:
        process.stdin.write(cmd)
        process.stdin.flush()
        time.sleep(0.1)  # Small delay to allow processing

    # Get the output
    stdout, stderr = process.communicate(timeout=10)

    print("STDOUT:")
    print(stdout)

    if stderr:
        print("STDERR:")
        print(stderr)

    print(f"Return code: {process.returncode}")
    print("Test completed!")

if __name__ == "__main__":
    test_interactive_mode()