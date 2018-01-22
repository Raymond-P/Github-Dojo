import sys
sys.path.append('../')
import unittest
import arrays.array_two_sum as ts


class TestArrayTwoSum(unittest.TestCase):

    def test_array_two_nums(self):
        nums = [2, 7, 11, 15]
        target = 26
        result = ts.two_sum(nums, target)
        self.assertEqual([2, 3], result)

    def test_no_nums(self):
        nums = []
        target = 26
        result = ts.two_sum(nums, target)
        self.assertEqual(None, result)

    def test_no_sum(self):
        nums = [2, 7, 11, 15]
        target = 0
        result = ts.two_sum(nums, target)
        self.assertEqual(None, result)


if __name__ == '__main__':
    unittest.main()
