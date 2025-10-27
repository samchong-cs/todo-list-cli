# Created on 26 October 2025
# Author: Samuel Chong

# *Variables needed for the add_task function:*
task_list = []
next_id = 1

# *Created functions:*
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
            task = {"id" : next_id, "task" : task_input}

            # Updating the dictionary to a list:
            task_list.append(task)

            # Automatically updating the ID number of the next task entered:
            next_id = next_id + 1
    
    # Printing the list as a 
    print(f"\nThis is the tasks list you entered: {task_list}. You successfully finished entering tasks.")
    menu()

def view_tasks():
    print(task_list)

def menu_message():
    # Printing out user options:
    print("\n1. Add task")
    print("2. Delete task")
    print("3. Editing task")
    print("4. Mark task complete")
    print("5. View task lists")
    print("6. Exit application")

def menu():
    menu_message()
    # Setting the variable for the task user selects:
    task = int(input("Enter the task number from 1 to 6: "))

    # Looping the menu until user exits the application:
    while True:
        # Applying the add task function from above:
        if task == 1:
            add_task()
            break
        
        elif task == 5:
            view_tasks()
            break
        
        elif task != 6:
            menu_message()
            task = int(input("Enter the task number: "))

        else:
            print("You have successfully exited the application.")
            break

# *Calling the menu function*:
menu()