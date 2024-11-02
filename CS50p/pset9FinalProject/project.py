# Program to implement To-Do List


import textwrap


from termcolor import colored
from tabulate import tabulate


class Task:
    def __init__(self, detail):
        self.detail = detail
        self.status = 'Incomplete'

    def __str__(self):
        return self.detail


class To_Do_List():
    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        self.task_list.append(task)

    def delete_task(self, task_number):
        task = self.task_list.pop(task_number - 1)
        return task


def main():
    # Create a empty list_object
    my_list = To_Do_List()

    while True:
        # Display Menu
        menu()

        # Ask user choice
        choice = input(colored("Please enter the option number: ", "yellow"))

        # Exit condition
        if choice == '5':
            break

        # Display all tasks
        elif choice == '1':
            tasks_list = fetch_list(my_list)
            #colored_list = colored(tasks_list, "white")
            print(f"\n{tasks_list}\n")

        # Add Task to the list
        elif choice == '2':
            task = input(colored('Enter Task: ', "cyan"))
            task = Task(task)
            my_list.add_task(task)
            print(wrap_text("Task succesfully added to list!", "green"))

        # Remove Task
        elif choice == '3':
            # Ask user for task to be removed
            text = "Please enter below the task-number to be removed\nTaskNumber: "
            task_number = input(colored(text, "cyan"))

            # Remove task and show confirmation
            try:
                deleted_task = my_list.delete_task(int(task_number))
                print(wrap_text(f"Task '{deleted_task}' has been successfully removed!\n", "green"))
            except:
                print(wrap_text("Invalid Task-Number!\n", "red"))

        # Change Task Completion Status
        elif choice == '4':
            # Ask user for task to be marked as complete
            text = "Please enter below the task-number which is complete\nTaskNumber: "
            task_number = input(colored(text, "cyan"))

            # Change completion status
            try:
                completed_task = my_list.task_list[int(task_number)]
                completed_task.status = "Complete"
                print(wrap_text(f"Task '{completed_task}' has been successfully completed!\n", "green"))
            except:
                print(wrap_text("Invalid Task-Number!\n", "red"))
        else:
            print(wrap_text("Please enter a valid choice", "red"))


def menu():
    """Genereate Menu"""

    menu = ("View Tasks", "Add Task", "Remove Task", "Mark Task as Done", "Exit program")

    # Diplay menu items
    print(colored("Select the option number from below", "yellow"))
    for number, option in enumerate(menu):
        print(colored(f"{number + 1}: {option}", "yellow"))
    print()


def fetch_list(list_object):
    """Create table of tasks"""

    tasks = []

    # Fetch tasks from list_object into list
    for number, task in enumerate(list_object.task_list):
        list_item = [number + 1, textwrap.fill(task.detail, width=20), task.status]
        tasks.append(list_item)

    # Tabulate all tasks
    tasks = tabulate(tasks, headers=['No.', 'Task', 'Status'])

    return tasks


def wrap_text(text, color):

    # Wrap your text
    wrapped_text = textwrap.fill(text, width=20)

    # Split the wrapped text into lines
    lines = wrapped_text.split('\n')

    # Create the top border
    top_border = "+" + "-" * 22 + "+"

    # Create the bottom border
    bottom_border = top_border

    # Add side borders to each line
    boxed_text = [top_border]
    for line in lines:
        boxed_text.append("| " + line.ljust(20) + " |")
    boxed_text.append(bottom_border)

    # Join the boxed text into a single string
    boxed_text = "\n".join(boxed_text)

    # Colorize your text
    colored_text = colored(boxed_text, color)

    return colored_text


main()
