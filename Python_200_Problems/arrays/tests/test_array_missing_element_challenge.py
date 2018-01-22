import sys
sys.path.append('../')
import unittest
from random import randrange as rand
from random import shuffle
import arrays.array_missing_element_challenge as ame


class TestMissingElement(unittest.TestCase):

    def test_finder(self):
        test_list = [rand(0, 100) for i in range(10)]
        shuffled_list = test_list[:]
        shuffle(shuffled_list)
        missing_element = shuffled_list.pop()  # since elements are shuffled the one that was popped was a random one
        result = ame.finder(test_list, shuffled_list)
        self.assertEqual(result, missing_element)


if __name__ == '__main__':
    unittest.main()
