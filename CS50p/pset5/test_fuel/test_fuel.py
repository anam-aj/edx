import pytest

from fuel import convert, gauge


def test_convert_split():
    with pytest.raises(ValueError):
        convert("2*3")
    with pytest.raises(ValueError):
        convert("abc")


def test_convert_type():
    with pytest.raises(ValueError):
        convert("a/2")
    with pytest.raises(ValueError):
        convert("2/a")
    with pytest.raises(ValueError):
        convert("a/b")


def test_convert_high_fraction():
    with pytest.raises(ValueError):
        convert("3/2")


def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")


def test_convert_value():
    assert convert("2/10") == 20


def test_gauge():

    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(50) == "50%"
    assert gauge(10) == "10%"
