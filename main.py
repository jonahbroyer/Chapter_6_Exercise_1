"""
    Random experiment to test the difference between a
    sequential search and a binary search on a list of integers.
"""
import time
import random

def ordered_sequential_search(alist, item):
    start = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos + 1
    end = time.time()
    return found, end - start


def binary_search(alist, item):
    start = time.time()
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    end = time.time()
    return found, end - start


random_list = []
for i in range(0, 100):
    n = random.randint(1, 100)
    random_list.append(n)

print(f"Random list: {random_list}")
print(ordered_sequential_search(random_list, 5))
print(ordered_sequential_search(random_list, 13))
print(binary_search(random_list, 78))
print(binary_search(random_list, 65))
