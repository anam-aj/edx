# Program to implement To-Do List


class Task:
    def __init__(self, detail):
        self.detail = detail
        self.status = False

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

        my_list = To_Do_List():

        # Display Menu
        menu()

        # Ask user choice
        choice = input("Please enter the option number: ")

        if choice == 1:
            for number, task in enumerate(my_list):
                print


        else:
            print("Please enter a valid choice or Enter 'exit' to quit")


def menu():
     menu = ("View Tasks", "Add Task", "Remove Task", "Mark Task as Done")

        for number, option in enumerate(menu):
             print(f"{number + 1} : {option}")
main()


