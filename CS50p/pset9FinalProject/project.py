# Program to implement To-Do List


class task:
    def __init__(self, detail):
        self.detail = detail
        self.status = False

    def __str__(self):
        return self.detail


class To_Do_List():
    def __init__(self):
        self.to_do_list = []

    def add_task(self, task):
        self.to_do_list.append(task)

    def delete_task(self, task_number):
        self.to_do_list.pop()


def main():

