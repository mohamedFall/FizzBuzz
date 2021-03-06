import unittest
from fizzbuzz_checker import FizzbuzzChecker


class FizzbuzzTest(unittest.TestCase):

    def test_should_raise_exception_with_number_0_and_negative_numbers(self):
        with self.assertRaises(ValueError):
            FizzbuzzChecker.fizzbuzz(0)
            FizzbuzzChecker.fizzbuzz(-1)

    def test_should_be_fizz_when_number_multiple_of_3(self):
        actual = FizzbuzzChecker.fizzbuzz(9)
        self.assertEqual(actual, "fizz")

    def test_should_be_buzz_when_number_multiple_of_5(self):
        actual = FizzbuzzChecker.fizzbuzz(25)
        self.assertEqual(actual, "buzz")

    def test_should_be_fizzbuzz_when_number_multiple_of_3_and_5(self):
        actual = FizzbuzzChecker.fizzbuzz(45)
        self.assertEqual(actual, "fizzbuzz")

    def test_should_repeate_number_when_number_is_not_good_for_other_cases(self):
        actual = FizzbuzzChecker.fizzbuzz(49)
        self.assertEqual(actual, 49)
