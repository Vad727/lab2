import unittest


class TestMultiplyNumbers(unittest.TestCase):

    def test_multiply_all_positive_numbers(self):
        self.assertEqual(multiply_numbers('2', '3', '4'), 24)

    def test_multiply_positive_and_negative_numbers(self):
        self.assertEqual(multiply_numbers('2', '-3', '4'), -24)

    def test_multiply_three_negative_numbers(self):
        self.assertEqual(multiply_numbers('-2', '-3', '-4'), -24)

    def test_multiply_positive_and_two_negative_numbers(self):
        self.assertEqual(multiply_numbers('-2', '3', '-4'), -24)

    def test_multiply_with_zero(self):
        self.assertEqual(multiply_numbers('0', '5', '10'), 0)

    def test_multiply_numbers_as_strings(self):
        self.assertEqual(multiply_numbers('1', '2', '3'), 6)


if __name__ == "__main__":
    unittest.main()