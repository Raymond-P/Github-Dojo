# ---------------------------------------------------------------
# python best courses https://courses.tanpham.org/
# ---------------------------------------------------------------
# Write a Python program to find validity of a string of parentheses, '(', ')',
#  '{', '}', '[' and '].
# These brackets must be close in the correct order,
# for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{"
# are invalid.

"""
test cases:
empty
""
single
"("
couple correct
"()"
couple incorrect
"(}"
combination of single and couple cases
    single couple incorrect
        single prior
            "{(]"
        single in between
            "({]"
        single after
            "(]{"
    single couple correct
        single prior
            "{()"
        single in between
            "({)"
        single after
            "(){"

multiple couple cases together
"""

"""
Approach:

    2 types of parentheses -> open and closed

    1 stack:
        if parentheses is open:
            push open to stack;
        else if parentheses is closed:
            try:
                pop the top of the stack
            except:
                return false # the string is not valid: extra closure
            if it is not the correct open parentheses:
                return false # string not valid: wrong closure

"""


def validate_string(string):
    lst = []  # to be treated as a stack
    parentheses_lst = {
        "(": ")",
        "[": "]",
        "{": "}"}
    for paren in string:
        if paren in parentheses_lst:
            lst.append(paren)
        else:  # closed
            try:
                cur_paren = lst.pop()
            except IndexError:  # lst is empty
                return False  # the string is not validity
            if paren != parentheses_lst[cur_paren]:
                return False  # string is not vaclid: wrong closure
    if len(lst) > 0:
        return False  # extra parentheses
    return True


if __name__ == '__main__':
    print(validate_string("()"))
    print(validate_string(")"))
    print(validate_string("(()"))
    print(validate_string("())"))
    print(validate_string("{()[{}][{}{}]}"))
