# Created on 26 October 2025
# Author: Samuel Chong

import json
import os
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(task_list, file, indent=2)

def load_tasks():
    global task_list, next_id
    
    # Check if file exists
    if not os.path.exists("tasks.json"):
        print("No saved tasks. Starting fresh!")
        return
    
    # Load from file
    with open("tasks.json", "r") as file:
        task_list = json.load(file)
    
    # Set next_id
    if task_list:
        next_id = max(task["id"] for task in task_list) + 1
    
    print(f"Loaded {len(task_list)} tasks!")

# *Variables needed for the add_task function:*
task_list = []
next_id = 1
 
# *Created functions:*

# Function 1:
def view_tasks():
    if len(task_list) == 0:
        print("\nNo tasks yet!")
        return
    
    print("\nYOUR TASKS:")
    for task in task_list:
        if task["completed"]:
            status = "✅"
        else:
            status = "○"
        print(f"{status} [{task['id']}] {task['task']}")
    return

# Function 2:
def menu_message():
    # Printing out user options:
    print("\n1. Add task")
    print("2. Delete task")
    print("3. Editing task")
    print("4. Mark task complete")
    print("5. View task lists")
    print("6. Exit application")

# Function 3:
def menu():
    # Looping the menu until user exits the application:
    while True:
        menu_message()
        # Setting the variable for the task user selects:
        task = int(input("Enter the task number from 1 to 6: "))
        # Applying the add task function from above:
        
        if task == 1:
            add_task()

        elif task == 2:
            delete_task()

        elif task == 3:
            edit_tasks()
        
        elif task == 4:
            mark_complete()

        elif task == 5:
            view_tasks()
        
        else:
            print("You have successfully exited the application.")

# Function 4:
def add_task():
    # To make sure that next_id variable is able to linked to this function:
    global next_id

    print("\nNOTE: Type in the tasks one by one, press enter after each. Write 'DONE' to complete adding tasks.")

    # Loop process of user entering tasks until they type "DONE"
    while True:
        task_input = input("\nType in your task: ")
        if task_input == "DONE":
            break
        else:
            # Saving each task as a dictionary:
            task = {"id" : next_id, "task" : task_input, "completed" : False}

            # Updating the dictionary to a list:
            task_list.append(task)

            # Automatically updating the ID number of the next task entered:
            next_id = next_id + 1
    
    # Printing the dictionaries as a list
    print(f"\nThis is the tasks list you entered: {task_list}. You successfully finished entering tasks.")

    print("Successfully added tasks!")
    save_tasks()  # Save to file!
    return

# Function 5:
def delete_task():
    global task_list
    print(task_list)

    # Nothing in the list yet:
    if len(task_list) == 0:
        print("No tasks to delete!")
        return

    id_to_delete = int(input("Enter the ID number of the task you want to delete: "))

    for task in task_list:
        if task["id"] ==  id_to_delete:
            # Removes the task based on the id number:
            task_list.remove(task)

            print(f"Deleted task for ID {id_to_delete}")

            save_tasks()  # Save to file!
            return
    
    print("Task ID not found! Please retry!") # happens if ID is not found during the loop
    return

# Function 6:
def edit_tasks():
    global task_list
    print(task_list)
    task_to_edit = int(input("Enter the ID of the task you want to edit: "))

    for task in task_list:
        if task["id"] == task_to_edit:
            # Creating a new variable to enter updated task description:
            updated_task = input("Enter a new task description: ")
            # Changing the task description based on the variable above (user's input)
            task["task"] = updated_task
            print(f"Updated task is {updated_task} now.")
            save_tasks()
            return

    print("Task ID not found!")  # happens if ID is not found during the loop
    return
    
# Function 7:
def mark_complete():
    global task_list
    if len(task_list) == 0:
        print("No more tasks to complete")
        return

    print(task_list)

    id_to_complete = int(input("Enter the task ID to mark complete: "))

    for task in task_list:
        if task["id"] == id_to_complete:
            task["completed"] = True
            print(f"Marked task {id_to_complete} as complete already!")
            save_tasks()
            return

    print("Task ID not found")
    return
    
# *Calling the functions*:
load_tasks()
menu()