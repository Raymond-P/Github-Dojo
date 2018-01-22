import unittest
import arrays.array_rotate as rotate


class TestRotate(unittest.TestCase):

    def setUp(self):
        self.array = [1, 2, 3, 4, 5]

    def test_rotate1_0(self):
        result = rotate.rotate1(self.array, 0)
        self.assertEqual([1, 2, 3, 4, 5], result)

    def test_rotate1_1(self):
        result = rotate.rotate1(self.array, 1)
        self.assertEqual([5, 1, 2, 3, 4], result)

    def test_rotate1_3(self):
        result = rotate.rotate1(self.array, 3)
        self.assertEqual([3, 4, 5, 1, 2], result)

    def test_rotate1_5(self):
        result = rotate.rotate1(self.array, 5)
        self.assertEqual([1, 2, 3, 4, 5], result)

    def test_rotate1_7(self):
        result = rotate.rotate1(self.array, 7)
        self.assertEqual([1, 2, 3, 4, 5], result)


if __name__ == '__main__':
    unittest.main()
