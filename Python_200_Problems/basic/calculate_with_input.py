# ---------------------------------------------------------------
# python best courses https://courses.tanpham.org/
# ---------------------------------------------------------------
# Write a Python program that accepts an integer (n) and computes the value of
# n+nn+nnn. Go to the editor
# Sample value of n is 5
# Expected Result : 615


def calc_input():
    usr_in = input()
    # try:
    n = int(usr_in)
    return n + (n * n) + (n * n * n)  # n + (n**2) + (n**3)


if __name__ == '__main__':
    print(calc_input())
