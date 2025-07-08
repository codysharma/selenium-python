import pytest


def add_two_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a + b

@pytest.mark.math
def test_small_numbers():
    assert add_two_numbers(1, 2) == 3, "1 + 2 should equal 3"

@pytest.mark.math
def test_large_numbers():
    assert add_two_numbers(100,300) == 400, "100 + 300 should equal 400"

@pytest.mark.math
def test_negative_numbers():
    assert add_two_numbers(-1, -2) == -3, "-1 + -2 should equal -3"

@pytest.mark.math
def test_zero():
    assert add_two_numbers(0, 0) == 0, "0 + 0 should equal 0"

@pytest.mark.math
def test_letters():
    try:
        add_two_numbers("a", "b")
    except TypeError:
        assert True, "Adding letters should raise TypeError"
    else:
        assert False, "Adding letters did not raise TypeError as expected"