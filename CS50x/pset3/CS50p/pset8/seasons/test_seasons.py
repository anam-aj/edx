from seasons import check_date_format, date_object


def test_correct_date_format():
    assert check_date_format("2010-01-01") == True
    assert check_date_format("1555-12-12") == True


def test_incorrect_date_format():
    assert check_date_format("2010-1-01") == False
    assert check_date_format("2010-01-1") == False
    assert check_date_format("2010-1-01") == False
    assert check_date_format("1 January, 2010") == False


def test_date_object():
    assert date_object("1 January, 2010") == False
    assert date_object("2010-13-01") == False
    assert date_object("2010-01-40") == False
