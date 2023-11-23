import pytest
from library import fibonnachi, bubble_sort, calculate

def test_fibonnachi():
    assert fibonnachi(0) == [0]
    assert fibonnachi(1) == [0, 1]
    assert fibonnachi(5) == [0, 1, 1, 2, 3]

def test_fibonnachi_negative_n():
    with pytest.raises(ValueError):
        fibonnachi(-1)

def test_bubble_sort():
    assert bubble_sort([5, 2, 3, 1]) == [1, 2, 3, 5]
    assert bubble_sort([]) ==[]
    assert bubble_sort([2, 2, 2, 2, 2]) == [2, 2, 2, 2, 2]

def test_calculate_addition():
    assert calculate(1, 4, "+") == 5
    assert calculate(0, 0, "+") == 0
def test_calculate_subtraction():
    assert calculate(3, 2, "-") == 1
    assert calculate(0, 0, "-") == 0
def test_calculate_division():
    assert calculate(6, 3, "/") == 2
    assert calculate(3, 5, "/") == 0.6

def test_calculate_division_zero():
    with pytest.raises(ZeroDivisionError):
        calculate(3, 0, "/") == float("inf")

def test_calculate_multiplication():
    assert calculate(1, 5, "*") == 5
    assert calculate(3, 0, "*") == 0