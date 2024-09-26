from um import count


def test_um_0():
    assert count("his number, I dont know") == 0
    assert count("well! Umbrella") == 0
    assert count("Umberella") == 0


def test_um_1():
    assert count("Um. I dont know") == 1
    assert count("well! Um. I dont know") == 1
    assert count(".Um. I dont know") == 1


def test_um_2():
    assert count("Um. I dont know. Um..") == 2
    assert count("uM? well! Um. I dont know") == 2
    assert count(".Um. I dont know.um") == 2
