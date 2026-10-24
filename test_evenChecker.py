import unittest
from evenChecker import is_even

class TestEvenChecker(unittest.TestCase):
    def test_even_number(self):
        self.assertTrue(is_even(4))

    def test_odd_number(self):
        self.assertFalse(is_even(7))

    def test_zero(self):
        self.assertTrue(is_even(0))

    def test_not_equal(self):
        self.assertNotEqual(is_even(9),True)

    def test_return_type(self):
        self.assertIsInstance(is_even(6),bool)



if __name__ == "__main__":
    unittest.main()