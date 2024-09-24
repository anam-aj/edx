from working import convert


def test_valid_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("09:00 AM to 05:00 PM") == "09:00 to 17:00"


def test_invalid_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("09:00 AM to 05:00 PM") == "09:00 to 17:00"
