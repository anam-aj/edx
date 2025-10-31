# Program to test twttr.py

from twttr import shorten


def test_number():
    assert shorten("123") == "123"


def test_spcl_character():
    assert shorten("~!@#$%^&*()_+") == "~!@#$%^&*()_+"


def test_random():
    assert shorten("kutta") == "ktt"
    assert shorten("BILLI") == "BLL"
