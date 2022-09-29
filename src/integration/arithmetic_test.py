import pytest
from src.operations import arithmetic


def test_sum_1(first=3, second=5, expected=8):
    assert arithmetic.addition(first, second) == expected, f"Incorrect value"


def test_sum_2(first=2, second=2, expected=4):
    assert arithmetic.addition(first, second) == expected, f"Incorrect value"


def test_sum_3(first=2, second=2, expected=4):
    assert arithmetic.addition(first, second) == expected, f"Incorrect value"


def test_subtraction_1(first=2, second=2, expected=0):
    assert arithmetic.subtraction(first, second) == expected, f"Incorrect value"


def test_subtraction_2(first=2, second=0, expected=2):
    assert arithmetic.subtraction(first, second) == expected, f"Incorrect value"


def test_subtraction_3(first=0, second=2, expected=-2):
    assert arithmetic.subtraction(first, second) == expected, f"Incorrect value"
