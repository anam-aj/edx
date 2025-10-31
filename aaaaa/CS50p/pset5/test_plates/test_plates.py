from plates import is_valid


def test_length():
    assert is_valid("a") == False
    assert is_valid("abcdefg") == False
    assert is_valid("ab") == True
    assert is_valid("abcdef") == True


def test_character_type():
    assert is_valid("abc@") == False
    assert is_valid("abc%") == False
    assert is_valid("ab12*") == False
    assert is_valid("abc12") == True


def test_first_two_character():
    assert is_valid("1234") == False
    assert is_valid("12ab") == False
    assert is_valid("1abc") == False
    assert is_valid("a1bc") == False


def test_numerical_rule():
    assert is_valid("ab0123") == False
    assert is_valid("abc012") == False
    assert is_valid("abcde0") == False
    assert is_valid("ab12a3") == False
    assert is_valid("ab1023") == True
