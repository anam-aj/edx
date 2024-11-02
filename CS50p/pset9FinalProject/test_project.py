import pytest


from project import Task, ToDoList, menu, fetch_list, wrap_text
from termcolor import colored

task1 = Task("Buy Pen")
task2 = Task("Car Wash")

list1 = ToDoList()
list1.add_task(task1)
list1.add_task(task2)


def test_menu(capsys):
    menu()
    captured = capsys.readouterr()
    assert "Select the option number from below" in captured.out
    assert "1: View Tasks" in captured.out
    assert "5: Save list and Exit program" in captured.out


def test_fetch_list():
    task_list = fetch_list(list1)
    assert task_list[0][0] == 1
    assert task_list[0][1] == "Buy Pen"
    assert task_list[0][2] == "Incomplete"

    assert task_list[1][0] == 2
    assert task_list[1][1] == "Car Wash"
    assert task_list[1][2] == "Incomplete"



def test_wrap_text():
    text = "This is a test text to be wrapped and colorized."
    color = "red"

    result = wrap_text(text, color)

    expected = (
        "+----------------------+\n"
        "| This is a test text  |\n"
        "|  to be wrapped and   |\n"
        "|      colorized.      |\n"
        "+----------------------+\n"
    )
    expected_colored = colored(expected, color)

    assert result == expected_colored
