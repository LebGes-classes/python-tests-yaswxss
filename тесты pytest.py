import pytest

from Functions import (
    add, subtract, multiply, divide
)


def test_add_int():
    """Проверка сложения целых чисел."""

    assert add(2, 3) == 5
    assert add(5, -2) == 3

def test_add_float():
    """Проверка сложения десятичных чисел."""

    assert add(2.5, 3.5) == 6.0

def test_add_type():
    """Проверка выброса TypeError"""

    with pytest.raises(TypeError):
        add(5, "3")

    with pytest.raises(TypeError):
        add("5", 3)

    with pytest.raises(TypeError):
        add(None, 5)


def test_subtract_int():
    """Проверка вычитания целых чисел."""

    assert subtract(10, 3) == 7
    assert subtract(7, 15) == -8
    assert subtract(-4, -3) == -1

def test_subtract_float():
    """Проверка вычитания десятичных чисел."""

    assert subtract(5.6, 2.3) == 3.3

def test_subtract_type():
    """Проверка выброса TypeError."""

    with pytest.raises(TypeError):
        subtract(5, "2")


def test_multiply_int():
    """Проверка умножения целых чисел."""

    assert multiply(4, 3) == 12
    assert multiply(-3, 6) == -18
    assert multiply(-4, -3) == 12

def test_multiply_float():
    """Проверка умножения десятичных чисел."""

    assert multiply(2.4, 3.2) == 7.68

def test_multiply_type():
    """Проверка выброса TypeError."""

    with pytest.raises(TypeError):
        multiply(2, "3")


def test_divide_int():
    """Проверка деления целых чисел."""

    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5
    assert divide(-4, -2) == 2

def test_divide_float():
    """Проверка деления десятичных чисел."""

    assert divide(8.64, 2.4) == 3.6

def test_divide_by_zero():
    """Проверка выброса ZeroDivisionError при делении на ноль."""

    with pytest.raises(ZeroDivisionError):
        divide(25, 0)

def test_divide_type():
    """Проверка выброса TypeError """

    with pytest.raises(TypeError):
        divide("8", 2)
