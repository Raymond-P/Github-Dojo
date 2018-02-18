# ---------------------------------------------------------------
# python best courses https://courses.tanpham.org/
# ---------------------------------------------------------------
# Challenge
#
# Given a string, find the length of the longest substring
# without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3.
# ---------------------------------------------------------------
# import sys
# sys.path.append('../')
# import os
# print(os.getcwd())
# os.chdir("..")
# print(os.getcwd())
import unittest
from .. import array_longest_non_repeat as lnr


class TestLongestNonRepeat(unittest.TestCase):

    def test_add_string_to_dict(self):
        dict1 = lnr.add_string_to_dict("hello", {})
        dict2 = dict()
        self.assertNotEqual(dict1, dict2, "Dictionary is NOT empty when adding a string!")
        dict2["hello"] = 1
        self.assertDictEqual(dict1, dict2, "Dictionary does NOT contain the correct entry!")
        dict1 = lnr.add_string_to_dict("hey", dict1)
        dict2["hey"] = 1
        self.assertDictEqual(dict1, dict2, "Dictionary doesn't contain the new entry!")
        dict1 = lnr.add_string_to_dict("hey", dict1)
        dict2["hey"] = 2
        self.assertDictEqual(dict1, dict2, "Dictionary entry not updated!")

    def test_longest_substring_in_dict(self):
        dict1 = {"hey": 1, "hi": 2, "there": 3}
        result = lnr.longest_substring_in_dict(dict1)
        self.assertEqual(result, "there")

    def test_substring_frequencies(self):
        # Non-repeated chars
        test_str = "abc"
        dict1 = lnr.substring_frequencies(test_str)
        self.assertDictEqual(dict1, {test_str: 1})

        # repeated substrings
        test_str = "abc" * 2
        dict1 = lnr.substring_frequencies(test_str)
        self.assertDictEqual(dict1, {"abc": 2}, "Error: Repeated values not updated properly")

        # repeated substrings with substring in between
        test_str = "abcabdeabc"
        dict1 = lnr.substring_frequencies(test_str)
        self.assertDictEqual(dict1, {"abc": 2, "abde": 1})

    def test_lonsgest_substring(self):
        # Given "abcabcbb", the answer is "abc", which the length is 3.
        result = lnr.longest_substring("abcabcbb")
        self.assertEqual(result, "abc")

        # Given "bbbbb", the answer is "b", with the length of 1.
        result = lnr.longest_substring("bbbbb")
        self.assertEqual(result, "b")

        # Given "pwwkew", the answer is "wke", with the length of 3.
        result = lnr.longest_substring("pwwkew")
        self.assertEqual(result, "wke")


if __name__ == '__main__':
    unittest.main()
