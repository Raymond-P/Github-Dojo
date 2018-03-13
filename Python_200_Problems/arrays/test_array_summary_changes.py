import unittest
from array_summary_changes import summary


class TestArraySummary(unittest.TestCase):

    def test_summary(self):
        result = summary([0, 1, 2, 4, 5, 7])
        self.assertEqual(["0->2", "4->5", "7"], result)

    def test_single_element(self):
        result = summary([0])
        self.assertEqual(["0"], result)

    def test_continuous_numbers(self):
        result = summary([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(["0->9"], result)

    def test_empty_list(self):
        result = summary([])
        self.assertEqual([], result)

    def test_non_continuous_list(self):
        result = summary([0, 2, 4, 6])
        self.assertEqual(["0", "2", "4", "6"], result)


if __name__ == '__main__':
    unittest.main()
