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
