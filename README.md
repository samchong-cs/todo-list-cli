**To-do List CLI application**

Started on: 26 Oct 2025

Planned features:
1. Carry out tasks based on menu
2. Adding tasks
3. Deleting tasks
4. Editing tasks
5. Marking tasks complete
6. View tasks as list

Future features:
1. Setting date for tasks, tasks due sooner are higher up on the list --> * not included yet, need to learn more about file management
2. Encouragement message after each task is completed --> * not included yet
3. Records how well user is completing tasks in percentage in menu section to encourage user to continue completing on time --> * not included yet


Technologies used:
- Python 3.8.7
- JSON for data storage

Main bugs faced during the process and how I solved them:
1. 26 Oct 2025 : The loop not ending for menu --> added break to prevent endless loop
2. 27 Oct 2025 : The word "DONE" appearing in the printed list after users completed entering their tasks --> add break after the if conditional where task_input is exactly the word "DONE"
3. 27 Oct 2025 : Users are not able to see the function to view their task list yet --> created and added the view_task function in the menu
4. 27 Oct 2025 : Code for the menu section could be shortened to maximise readability and efficiency --> created a function menu-message to avoid repetition
5. 27 Oct 2025 : Tasks did not a specific ID which could help perform the other functions in the program --> Changing the task lists from using list in Python to using dictionaries to add IDs more efficiently
6. 27 Oct 2025 : Printing of the tasks list for the viewing function kept looping and add function appeared after the view function happened --> added break after calling the view_task function and also add_task function
7. 30 Oct 2025 : The printing of the view function did not work when code changed to fit the new mark complete function --> changed from retreiving information to the dictionary 'task' instead of the list 'task_list' 
8. 1 Nov 2025 : Added save task function after return which did not work --> placed it before
9. 12 Nov 2025 : Menu function called recursively at the end of each function, causing function call stacking and wasting memory --> replaced with return statements to keep the loop in one place, making code more efficient and Pythonic
10. 12 Nov 2025 : User input not repeating after task completion because input was only asked once at start of menu --> moved input statement inside the while True: loop so it asks for a new choice each iteration
11. 12 Nov 2025 : Included global in most of the functions to be more 'Pythonic' even though editing the variable does not affect it only completing updating to a new value needs global

**Project development log:**
Day 1 (26 October 2025):
Created this repository in GitHub to document my first coding project. I roughly planned the general flow of my program and laid out the key features I must have in my program. Created the menu of the application and the function to add tasks.

Day 2 (27 October 2025):
Identified certain bugs / problems with the code and rectified them - listed in the list of bugs above as part of 27 October 2025 debugging. Added the function to view the tasks list by printing out the list saved.

Day 3 (28 October 2025):
Finding out how to create delete_task function due to increased complexity of indiviudals dictionaries in a list.

Day 4 (29 October 2025):
Successfully created the delete_task function and made the code for view_tasks function more robust. Created the edit_task function

Day 5 (30 October 2025):
Created the mark complete feature and presented the list with a status icon

Day 6 (1 November 2025):
Created JSON for storage

Day 7 (12 Nov 2025) --> picking up the project after finishing exams:
Resolving final bugs and also understanding the flow of the code more in depth

**Key Features Code Structure (the one I learned the most):**
save_tasks(): Opens the tasks.json file in write mode and uses json.dump() to convert the Python list of tasks into JSON format. This ensures user tasks are saved to permanent storage and persist between program sessions.
load_tasks(): Called at program startup before the menu appears. It checks if tasks.json exists, and if so, reads and converts the JSON data back into a Python list. This allows users to access their previously saved tasks and continue managing them.
view_tasks(): Creates a loop where each task in the task list will have a status made known by the emoji then it is printed as a combination of multiple strings extracting information from the dictionary to print the task lists to users

How to Run:
1. Clone the repository
2. Ensure Python 3.8.7+ is installed
3. Run: python todo_list.py
4. Follow the menu prompts to add, edit, delete, or view tasks
5. Tasks are automatically saved to tasks.json

Objective for this project: I want to make a highly functional command-line application which provides users a platform to be able to save their tasks seamlessly and be as user-friendly as possible to ensure they can manage tasks easily

Future hopes for this project's advancement:
1. Making it GUI when I have the skills then
2. Storing the tasks in a more robust manner
3. Adding more interactive functions like buttons and text boxes
4. Code becomes more 'Pythonic'
5. Validating user input more
