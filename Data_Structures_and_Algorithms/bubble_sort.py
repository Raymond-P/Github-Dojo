"""
Implement bubble sort algorithm for a given int array
"""
from random import randint


def bubble_sort(arr):
    # Iterate through the list
    for j in range(len(arr) - 1, 0, -1):
        for i in range(j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


if __name__ == "__main__":
    lst = []
    for i in range(10):
        lst.append(randint(0, 9))
    copy = lst[:]
    print(f"copy: {copy}")
    print(f"Orig: {lst}")
    print("-" * 36)
    bubble_sort(lst)
    copy.sort()
    print(f"copy: {copy}")
    print(f"Orig: {lst}")
