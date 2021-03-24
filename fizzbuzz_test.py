import unittest
from fizzbuzz_checker import FizzbuzzChecker

class FizzbuzzTest(unittest.TestCase):

    def test_should_raise_exception_with_number_0(self):
        with self.assertRaises(ValueError):
            FizzbuzzChecker.fizzbuzz(0)
    
    def test_should_raise_exception_with_negative_numbers(self):
        with self.assertRaises(ValueError):
            FizzbuzzChecker.fizzbuzz(-1)
