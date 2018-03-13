
"""
given a string. eliminate the characters that consecutively repeat themselves
3 or more times. After eliminating a string, re-evaluate the string from the
beggining.

ex:
"A"->"A"
"AA"->"AA"
"AAA"->""
"AAAAAAAAAAAAAAA"->""
"AAAAAB"->"B"
"BBAAAB"->""  // "BBAAAB"->"BBB"->""
"""


def compress_string(string):
    if len(string) < 3:
        return string
    cur_char = string[0]
    start = 0
    end = 0
    for i, n in [(x, y) for x, y in enumerate(string)]:
        if n == cur_char:
            end = i
        else:
            pass
        print(f"{n},{i}")


if __name__ == "__main__":
    print("main here! :D")
    compress_string("hello there")
