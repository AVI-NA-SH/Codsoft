# todo.py

import sys
import datetime

# Help function: Provides usage instructions
def help():
    usage = """Usage:
    $ ./todo add "todo item"       # Add a new task
    $ ./todo ls                    # Show remaining tasks
    $ ./todo del NUMBER            # Delete a task
    $ ./todo done NUMBER           # Complete a task
    $ ./todo help                  # Show usage
    $ ./todo report                # Statistics"""
    sys.stdout.buffer.write(usage.encode('utf8'))

# Function to add items to the to-do list
def add(task):
    with open('todo.txt', 'a') as f:
        f.write(task + "\n")
    print(f"Added task: {task}")

# Function to list remaining tasks
def ls():
    try:
        with open('todo.txt', 'r') as f:
            tasks = f.readlines()
            for i, task in enumerate(reversed(tasks), start=1):
                sys.stdout.buffer.write(f"[{i}] {task}".encode('utf8'))
    except FileNotFoundError:
        print("No tasks found. Add some tasks using './todo add'.")

# Function to mark a task as completed
def done(task_number):
    try:
        with open('todo.txt', 'r') as f:
            tasks = f.readlines()
            task = tasks[-task_number].strip()
            with open('done.txt', 'a') as done_file:
                done_file.write(task + "\n")
            print(f"Marked task as done: {task}")
    except (FileNotFoundError, IndexError):
        print("Invalid task number. Use './todo ls' to see available tasks.")

# Entry point
if __name__ == "__main__":
    if len(sys.argv) < 2:
        help()
    else:
        command = sys.argv[1]
        if command == "add":
            if len(sys.argv) < 3:
                print("Usage: ./todo add \"todo item\"")
            else:
                add(sys.argv[2])
        elif command == "ls":
            ls()
        elif command == "done":
            if len(sys.argv) < 3:
                print("Usage: ./todo done NUMBER")
            else:
                done(int(sys.argv[2]))
        else:
            help()
