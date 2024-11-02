import pytest


from project import Task, ToDoList,menu, fetch_list

task1 = Task("Buy Pen")
task2 = Task("Car Wash")

list1 = ToDoList()

def test_menu(capsys):
    menu()
    captured = capsys.readouterr()
    assert "Select the option number from below" in captured.out
    assert "1: View Tasks" in captured.out
    assert "5: Save list and Exit program" in captured.out


def test_fetch_list():
    ...
