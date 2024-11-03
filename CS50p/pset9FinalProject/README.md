# To-do App

A terminal based "To-Do List" program


### Video Demo: https://opulent-chainsaw-4jgvrqprxq4qhqg5r.github.dev/


### pip install libraries:

* textwrap
* termcolor
* tabulate


### Description:

Poject's root directory contains 4 files namely

* project.py : contains the code of the program
* test_project.py : contains test functions that can be checked with pytest
* requirements.txt : contains information about libraires required
* README.md : Detailed description of project

It is a To-do list program which can be completely run from terminal. It lets user create a 'To-do list' which contains a list of tasks. It aslo give users option to 'add task',    I made it very easy to use. One can simply use the program by reading only what is being shown on screen. User friendly feedback messages are displayed making it easy for the user to understand the working of program. Feedback messages and Instructions are colourized and boxed to making it easy to read.

When initiated it provides the user a menu of choices namely
* 1: View Tasks
* 2: Add Task
* 3: Remove Task
* 4: Mark Task as Done
* 5: Save list and Exit program

and then user is promted for choice with a descriptive message as given below
* Please enter the option number:

user can then enter the option number and then further, easy to follow,
instructions are displayed on screen.

Main code file "project.py" contains the following classes and functions(other than main):

* Class
    * Task
    * ToDoList
* Function
    * menu
    * fetch_list
    * open_list
    * save_list
    * wrap_text

#### Task:
    Creates an 'Task' object with two attributes namely 'detail' and 'status'. 'detail' contains the description of task and 'status' represent whether task is complete or not.

#### ToDoList:
    Creates a 'ToDoList' object, intialized with an instance variable 'task_list' which is an empty list when instantiated. This 'task_list' is then used to store 'Task' objects. It has methods 'add_task' and 'delete_task' which adds or deletes 'Task' objects from 'task_list'

#### menu:
    It has the choices for menu options stored as list. It fetches menu items from list, enumerates them and then generate and print a nicely formatted menu to user.

#### fetch_list:
    Takes a 'ToDoList' object as argument, fetch 'Tasks' from it and format each task as one string per task contianing the task-number, task-detail and task-status. Returns a list of such strings.

#### open_list:
    Check if there is a saved file for 'ToDolist' and load it. If not fount instantiate a new 'ToDoList'.

#### save_list:
    Saves the user generated 'ToDoList' for persistant usage. It uses pickle module to

#### wrap_text:
    Helps other function by formatting text. Takes two arguments Colorize text and put it in a 'box' for better visibility readability.


### Acknowledgment:

* #### CS50 Duck
    The duck has been a GREAT help! Saved a lot of time by helping in finding required libraries and helping with syntax usage, thus I could invest my time to focus more on core logic.
