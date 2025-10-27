**To-do List CLI application**

Started on: 26 Oct 2025

Planned features:
1. Carry out tasks based on menu
2. Adding tasks
3. Deleting tasks
4. Editing tasks
5. Setting date for tasks, tasks due sooner are higher up on the list
6. Marking tasks complete
7. Encouragement message after each task is completed
8. Records how well user is completing tasks in percentage in menu section to encourage user to continue completing on time
9. View tasks as list

Technologies used:
- Python 3.8.7
- JSON for data storage (planned)

Main bugs faced during the process and how I solved them:
1. 26 Oct 2025 : The loop not ending for menu --> added break to prevent endless loop
2. 27 Oct 2025 : The word "DONE" appearing in the printed list after users completed entering their tasks --> add break after the if conditional where task_input is exactly the word "DONE"
3. 27 Oct 2025 : Users are not able to see the function to view their task list yet --> created and added the view_task function in the menu
4. 27 Oct 2025 : Code for the menu section could be shortened to maximise readability and efficiency --> created a function menu-message to avoid repetition
5. 27 Oct 2025 : Tasks did not a specific ID which could help perform the other functions in the program --> Changing the task lists from using list in Python to using dictionaries to add IDs more efficiently
6. 27 Oct 2025 : Printing of the tasks list for the viewing function kept looping and add function appeared after the view function happened --> added break after calling the view_task function and also add_task function

**Project development log:**
Day 1 (26 October 2025):
Created this repository in GitHub to document my first coding project. I roughly planned the general flow of my program and laid out the key features I must have in my program. Created the menu of the application and the function to add tasks.

Day 2 (27 October 2025):
Identified certain bugs / problems with the code and rectified them - listed in the list of bugs above as part of 27 October 2025 debugging. Added the function to view the tasks list by printing out the list saved.

Objective for this project: I want to make a highly functional command-line application which provides users a platform to be able to save their tasks seamlessly and be as user-friendly as possible to ensure they can manage tasks easily

Future hopes for this project's advancement:
1. Making it GUI when I have the skills then
2. Storing the tasks in a more robust manner
3. Adding more interactive functions like buttons and text boxes
4. Code becomes more 'Pythonic'
5. 
6. 
