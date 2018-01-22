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

"""
Notes:

    I added some extra functionality to the problem and making
    it a little more complicated by keeping track of the
    frequencies in which each substring appears.
"""


# ---------------------------------------------------------------


def substring_frequencies(string):
    words_list = {}
    cur_substring = ""
    #  generate a dictionary of the frequency of the substrings
    for index in range(len(string)):

        if string[index] not in cur_substring:  # new char part of substring
            cur_substring += string[index]

            if index == len(string)-1:
                words_list = add_string_to_dict(cur_substring,words_list)

        else:  # reoccuring char found in string thus new substring

            words_list = add_string_to_dict(cur_substring,words_list)
            cur_substring = ""  # reset the substring
            cur_substring += string[index]
    return words_list


def add_string_to_dict(string, dict):
    if string in dict:
        dict[string] += 1
    else:
        dict[string] = 1
    return dict


def longest_substring_in_dict(dictionary):
    longest = ""
    for word in dictionary.keys():
        if len(word) > len(longest):
            longest = word
    return longest


def longest_substring(string):
    dict_of_substrings = substring_frequencies(string)
    return longest_substring_in_dict(dict_of_substrings)