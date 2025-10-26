# Created on 26 October 2025
# Author: Samuel Chong

# *List of tasks:*
task_list = []

# *Created functions:*
def add_task():
    print("\nNOTE: Type in the tasks one by one, press enter after each. Write 'DONE' to complete adding tasks.")
    while True:
        task_input = input("\nType in your task: ")
        # Adds the task to user list based on what user enters:
        task_list.append(task_input)
        if task_input == "DONE":
            print(f"\nThis is your task list: {task_list}.")
            print("\nYou have successfully finished adding tasks!")
            menu()
            break

def menu():
    # Printing out user options:
    print("\n1. Add task")
    print("2. Delete task")
    print("3. Editing task")
    print("4. Mark task complete")
    print("5. Exit application")

    # Setting the variable for the task user selects:
    task = int(input("Enter the task number from 1 to 5: "))

    # Looping the menu until user exits the application:
    while True:
        # Applying the add task function from above:
        if task == 1:
            add_task()
        
        elif task != 5:
            print("1. Add task")
            print("2. Delete task")
            print("3. Editing task")
            print("4. Mark task complete")
            print("5. Exit application")
            task = int(input("Enter the task number: "))

        else:
            print("You have successfully exited the application.")
            break

# *Calling the menu fucntion*:
menu()
