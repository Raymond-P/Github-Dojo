# import sys
# sys.path.append('../')
import unittest
import array_merge_intervals as m


class testMergeIntervals(unittest.TestCase):

    def test_merge_intervals(self):
        lst = [[1, 3], [2, 6], [5, 10], [11, 16], [15, 18], [19, 22]]
        result = m.merge_intervals(lst)
        self.assertEqual([[1, 10], [11, 18], [19, 22]], result)

    def test_non_overlaping_intervals(self):
        lst = [[1, 2], [3, 4], [5, 6], [7, 8]]
        result = m.merge_intervals(lst)
        self.assertEqual(lst, result)


if __name__ == '__main__':
    unittest.main()
