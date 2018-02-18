# ---------------------------------------------------------------
# python best courses https://courses.tanpham.org/
# ---------------------------------------------------------------
# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they
# will turn 100 years old.
from datetime import date

name = input("hello user. What is your name? ")
print(f"Nice to meet you {name}!\n")
age = None
while not isinstance(age, int):
    try:
        age = int(input(f"say, How old are you {name}?"))
    except ValueError:
        print(f"{name} please answer with an integer number.")
cur_year = date.today().year
century_anum = cur_year + 100 - age
if(input(f"Did your brithday already passed {name}? [y/n] ") != "y"):
    century_anum -= 1
print(f"\n{name}, you will become 100 years old in the year {century_anum}")
