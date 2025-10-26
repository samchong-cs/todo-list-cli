# Created on 26 October 2025
# Author: Samuel Chong

# *Menu*:

# Printing out user options:
print("1. Add task")
print("2. Delete task")
print("3. Editing task")
print("4. Mark task complete")
print("5. Exit application")

# Setting the variable for the task user selects:
task = int(input("Enter the task number: "))

# Looping the menu until user exits the application:
while True:
    if task != 5:
        print("1. Add task")
        print("2. Delete task")
        print("3. Editing task")
        print("4. Mark task complete")
        print("5. Exit application")
        task = int(input("Enter the task number: "))

    else:
        print("You have succesfully exited the application.")
        break