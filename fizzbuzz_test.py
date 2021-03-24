import unittest
from fizzbuzz_checker import FizzbuzzChecker

class FizzbuzzTest(unittest.TestCase):

    def test_should_raise_exception_with_number_0(self):
        with self.assertRaises(ValueError):
            FizzbuzzChecker.fizzbuzz(0)
    
    def test_should_raise_exception_with_negative_numbers(self):
        with self.assertRaises(ValueError):
            FizzbuzzChecker.fizzbuzz(-1)

    def test_should_be_fizz_when_number_multiple_of_3(self):
        actual = FizzbuzzChecker.fizzbuzz(9)
        self.assertEqual(actual, "fizz")

    def test_should_be_buzz_when_number_multiple_of_5(self):
        actual = FizzbuzzChecker.fizzbuzz(25)
        self.assertEqual(actual, "buzz")