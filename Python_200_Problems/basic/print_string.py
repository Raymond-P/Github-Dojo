# ---------------------------------------------------------------
# python best courses https://courses.tanpham.org/
# ---------------------------------------------------------------
# Write a Python program to print the following string in a specific format
# (see the output). Go to the editor

# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"

# Output :

# Twinkle, twinkle, little star,
# 	How I wonder what you are!
# 		Up above the world so high,
# 		Like a diamond in the sky.
# Twinkle, twinkle, little star,
# 	How I wonder what you are

"""
line -> #words -> #tabs
0 -> 4 -> 0
1-> 6 -> 1
2 -> 6 -> 2
3 -> 6 -> 2

4 -> 4 -> 0
5 -> 6 -> 1
"""


def print_string(string):
    lst = enumerate(string.split(" "))
    counter = 0
    if counter % 4 == 0:
        for word in range()
    # for a, b in lst:
    #     if a%4 == 0:
    pass
