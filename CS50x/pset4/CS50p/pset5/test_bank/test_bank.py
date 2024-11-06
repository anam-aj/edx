from bank import value


def test_hello_greetings():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hello abc xyz") == 0
    assert value("Hello abc xyz") == 0
    assert value("HELLO abc xyz") == 0


def test_h_greetings():
    assert value("hi") == 20
    assert value("Hi") == 20
    assert value("Hi") == 20
    assert value("hi abc xyz") == 20
    assert value("Hi abc xyz") == 20
    assert value("Hi abc xyz") == 20
    assert value("hey") == 20
    assert value("Hey") == 20
    assert value("Hey") == 20
    assert value("hey abc xyz") == 20
    assert value("Hey abc xyz") == 20
    assert value("Hey abc xyz") == 20


def test_other_greetings():
    assert value("abc xyz") == 100
    assert value("good morning") == 100
    assert value("afternoon") == 100
