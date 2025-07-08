def add_two_numbers(a, b):
    return a + b


def test_small_numbers():
    assert add_two_numbers(1, 2) == 3, "1 + 2 should equal 3"

def test_large_numbers():
    assert add_two_numbers(100,300) == 400, "100 + 300 should equal 400"