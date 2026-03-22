#!/usr/bin/env python3
import tasks_manager
import sys
import shlex
from pathlib import Path

BASE_DIR = Path(__file__).parent
LISTS_DIR = BASE_DIR / "lists"

args = sys.argv
main_list = []



if len(args) < 2:
    print("Well shit")

elif args[1] == "help":
    print('''
╭───────────────────────────╮
│   Simple To-do - By Jay   │
╰───────────────────────────╯
A simple project that seems to be at the intermediate stage of my knowledge.

Create multiple lists of tasks.
With-in the list you can use commands to manage your tasks in that list!

You first load up a 

Commands:
    Managing Lists:
    • load - Creates or loads a file, with a name.
        simple-todo load homework
    • remove - Removes the file, with a name.
        simple-todo remove homework
    • print - Lists all lists in the lists folder.

    Managing Tasks:
    
    • add - Adds a task with text to the list with a given index.
        add "fuck yuhh" 2
    • remove - Removes a task with a index.
        remove 2
    • 
''')

elif args[1] == "load":
    name = args[2]
    main_list = tasks_manager.TaskManager(name)

    print(f"You are now editing list '{name}'")
    print("To leave type 'exit' or a quick Ctrl + C")
    main_list.print()

    while True:
        answer = input(f"{name}> ")

        args = shlex.split(answer)

        if not args:
            continue

        command = args[0]

        if command == "exit":
            print("Good-bye! 👋")
            sys.exit()

        elif command == "add":
            text = args[1]
            index = 0

            if len(args) > 2:
                index = int(args[2])

            main_list.add(text, index)

        elif command == "remove":
            index = int(args[1])

            main_list.remove(index)

        elif command == "clear":
            answer = input(f"Are you sure to remove all tasks? [Y/n] ").lower()

            if answer == "no" or answer == "n":
                print("Ok")
                continue

            main_list.modify([])
            print("Cleared list.")
            
        elif command == "print":
            main_list.print()

        else:
            print("Unknown command.")

elif args[1] == "remove":
    name = args[2]
    answer = input(f"Are you sure to remove '{name}.json'? [Y/n] ").lower()

    if answer == "no" or answer == "n":
        print("Ok")
        sys.exit()
    
    file = LISTS_DIR / f"{name}.json"
    file.unlink(missing_ok=True)

    print(f"Removed '{name}.json'")

elif args[1] == "print":
    print("List of lists in the list folder:")

    for file in LISTS_DIR.iterdir():
        print(f"    {file.name}")

elif args[1] == "clear":
    answer = input(f"Are you sure to remove all lists? [Y/n] ").lower()

    if answer == "no" or answer == "n":
        print("Ok")
        sys.exit()

    answer = input(f"Are you 2x sure to remove all lists? [Y/n] (2ND WARNING)").lower()

    if answer == "no" or answer == "n":
        print("Ok")
        sys.exit()

    for file in LISTS_DIR.iterdir():
        if file.is_file():
            file.unlink()