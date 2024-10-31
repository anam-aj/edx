# Program to implement To-Do List


class task():
    def __init__(self, detail):
        self.detail = detail
        self.status = False

    def __str__(self):
        return self.detail


class To_Do_List():
    def __init__(self):
        with open "MyList.txt" as "my_list":
            pass

    def add_task(self, task):
        ...

    def delete_task(self, task):
        ...


def main():

