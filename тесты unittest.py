import unittest

from Functions import (
    add, subtract, multiply, divide
)


class TestCalculator(unittest.TestCase):

    def test_add_int(self):
        """Проверка сложения целых чисел."""

        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, -2), 3)

    def test_add_float(self):
        """Проверка сложения десятичных чисел"""

        self.assertAlmostEqual(add(2.5, 3.5), 6.0)

    def test_add_type_error(self):
        """Проверка выброса TypeError"""

        with self.assertRaises(TypeError):
            add(5, "3")

        with self.assertRaises(TypeError):
            add("5", 3)

        with self.assertRaises(TypeError):
            add(None, 5)


    def test_subtract_int(self):
        """Проверка вычитания целых чисел."""

        self.assertEqual(subtract(10, 3), 7)
        self.assertEqual(subtract(7, 15), -8)
        self.assertEqual(subtract(-4, -3), -1)

    def test_subtract_float(self):
        """Проверка вычитания десятичных чисел"""

        self.assertAlmostEqual(subtract(5.6, 2.3), 3.3)

    def test_subtract_type_error(self):
        """Проверка выброса TypeError"""

        with self.assertRaises(TypeError):
            subtract(5, "2")

    def test_multiply_int(self):
        """Проверка умножения целых чисел."""

        self.assertEqual(multiply(4, 3), 12)
        self.assertEqual(multiply(-3, 6), -18)
        self.assertEqual(multiply(-4, -3), 12)

    def test_multiply_float(self):
        """Проверка умножения десятичных чисел"""

        self.assertAlmostEqual(multiply(2.4, 3.2), 7.68)

    def test_multiply_type_error(self):
        """Проверка выброса TypeError"""

        with self.assertRaises(TypeError):
            multiply(2, "3")

    def test_divide_int(self):
        """Проверка деления целых чисел."""

        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(7, 2), 3.5)
        self.assertEqual(divide(-4, -2), 2)

    def test_divide_float(self):
        """Проверка деления десятичных чисел"""

        self.assertAlmostEqual(divide(8.64, 2.4), 3.6)

    def test_divide_by_zero(self):
        """Проверка выброса ZeroDivisionError"""

        with self.assertRaises(ZeroDivisionError):
            divide(25, 0)

    def test_divide_type_error(self):
        """Проверка выброса TypeError"""

        with self.assertRaises(TypeError):
            divide("8", 2)


if __name__ == '__main__':
    unittest.main()