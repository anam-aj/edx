# Program to implement To-Do List

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

    def __str__(self):
        return self.task_list

    def add_task(self, task):
        self.task_list.append(task)

    def delete_task(self, task_number):
        self.task_list.pop(task_number - 1)


def main():
    my_list = To_Do_List()

    while True:

        # Display Menu
        menu()

        # Ask user choice
        choice = input("Please enter the option number: ")

        if choice.lower() == 'exit':
            break
        elif choice == '1':
            tasks_list = fetch_list(my_list)
            print(tasks_list)
            #print(tabulate(tasks_list, headers=['No.', 'Task', 'Status']))
        elif choice == '2':
            task = input('Please enter task: ')
            task = Task(task)
            my_list.add_task(task)
        elif choice == '3':
            ...
        else:
            print("Please enter a valid choice or Enter 'exit' to quit program")


def menu():
    menu = ("View Tasks", "Add Task", "Remove Task", "Mark Task as Done")

    for number, option in enumerate(menu):
        print(f"{number + 1}: {option}")


def fetch_list(list_object):
    tasks = []

    for number, task in enumerate(list_object.task_list):
        list_item = [number + 1, task.detail, task.status]
        tasks.append(list_item)

    tasks = tabulate(tasks, headers=['No.', 'Task', 'Status'])

    return tasks


main()
