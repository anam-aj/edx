import pytest


from project import Task, ToDoList,menu


def test_menu(capsys):
    menu()
    captured = capsys.readouterr()
    assert "Select the option number from below" in captured.out
    assert "1: View Tasks" in captured.out
    assert "5: Save list and Exit program" in captured.out
