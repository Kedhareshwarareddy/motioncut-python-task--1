# motioncut-python-task--11
# README: To Do List (TASK 1)

## Author: KEDHARESHWARA SUBBA REDDY

## Batch:(5th NOVEMBER- 5th DECEMBER)

## Domain: PYTHON Programming

## Aim

The aim of this project is to build a To-Do List Application

## Description

This application allows users to add tasks, mark tasks as completed, update task descriptions,add priority to tasks and remove tasks from the list. This has been implemented in a graphical user interface (GUI).

## Libraries Used

The following important libraries were used for this project:

- tkinter


  ## Working of the Code 

1. Class Structure:
   - The application defines a Task class to represent individual tasks, encapsulating information such as description, due date, priority, and completion status.
   - The main application logic is implemented in the ToDoListApp class.

2. GUI Setup:
   - The application uses the Tkinter library to create a graphical user interface.
   - Entry fields are provided for the user to input task description, due date, and priority.
   - A Listbox widget displays the list of tasks.
   - Buttons for adding, removing, completing, and updating tasks are included.

3. Task Management:
   - Tasks are stored as instances of the Task class in the tasks list.
   - The add_task method creates a new task based on user input and appends it to the list, then updates the display.
   - The remove_task method deletes the selected task from the list and updates the display.
   - The complete_task method marks the selected task as completed and updates the display.
   - The update_task method modifies the details of the selected task and updates the display.

4. Listbox Display:
   - The update_listbox method refreshes the Listbox with the current list of tasks.
   - Tasks are displayed in a readable format, including description, due date, priority, and completion status.

5. Buttons:
   - The "Add Task" button triggers the add_task method.
   - The "Remove Task" button triggers the remove_task method.
   - The "Mark as Completed" button triggers the complete_task method.
   - The "Update Task" button triggers the update_task method.

6. Initialization:
   - The create_widgets method initializes the GUI components and sets up the initial display.
   - The update_listbox method is called during initialization to populate the Listbox with existing tasks.

7. Execution:
   - The main function creates the Tkinter root window and the ToDoListApp instance, starting the main loop to run the application.

8. Usage:
   - Users can run the script to launch the To-Do List application, interact with the GUI, and manage their tasks.
