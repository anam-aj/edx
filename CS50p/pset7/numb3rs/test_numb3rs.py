from numb3rs import validate


def test_correct_input():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("219.229.239.249") == True
    assert validate("001.001.001.001") == True
    assert validate("01.01.01.01") == True


def test_out_of_range():
    assert validate("512.512.512.512") == False
    assert validate("256.256.256.256") == False
    assert validate("300.300.300.300") == False
    assert validate("1.1.1.1000") == False
    assert validate("100.555.555.555") == False


def test_word():
    assert validate("cat") == False
    assert validate("cat.1.1.1") == False
