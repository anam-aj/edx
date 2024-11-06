import pytest

from working import convert


def test_valid_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("09:00 AM to 05:00 PM") == "09:00 to 17:00"


def test_invalid_time():
    with pytest.raises(ValueError):
        convert("19 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM to 50:00 PM")
    with pytest.raises(ValueError):
        convert("5 AM to 19 PM")
    with pytest.raises(ValueError):
        convert("50:00 AM to 09:00 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")


def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
