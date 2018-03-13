"""
Implement a selection sort algorithm for an int array
"""
from random import randint


def selection_sort(arr):

    for i in range(len(arr)):
        min_index = i
        for j in range(i, len(arr), 1):
            if arr[j] < arr[min_index]:
                min_index = j
        # swap
        arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == "__main__":
    lst = []
    for i in range(10):
        lst.append(randint(0, 9))
    copy = lst[:]
    print(f"copy: {copy}")
    print(f"Orig: {lst}")
    print("-" * 36)
    selection_sort(lst)
    copy.sort()
    print(f"copy: {copy}")
    print(f"Orig: {lst}")
