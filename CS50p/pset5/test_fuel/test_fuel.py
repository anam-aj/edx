import pytest

from fuel import convert, gauge


def test_convert():

    with pytest.raises(ValueError):
        convert("2*3")
    with pytest.raises(ValueError):
        convert("abc")
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ValueError):
        convert("a/2")
    with pytest.raises(ValueError):
        convert("2/a")
    with pytest.raises(ValueError):
        convert("a/b")
    with pytest.raises(ValueError):
        convert("2*3")
    with pytest.raises(ZeroDivisionError):
        convert("2/0")


def test_gauge():

    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(10) == "10%"
