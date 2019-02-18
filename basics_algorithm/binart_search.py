"""
Binary Search

- https://algorithm.yuanbin.me/zh-hans/basics_algorithm/binary_search.html
- https://www.geeksforgeeks.org/binary-search/
"""

import unittest
from random import randrange


def binary_search(array, l, r, x):
    # check base case
    if r < l:
        # element is not present in the array
        return -1

    mid = l + (r - l) // 2
    # if element is present at the middle itself
    if x == array[mid]:
        return mid
    # if element is larger than mid, then it
    # can only be present in right subarray
    elif x > array[mid]:
        return binary_search(array, mid + 1, r, x)
    # else the element can only be present
    # in left subarray
    else:
        return binary_search(array, l, mid - 1, x)


class TestBinarySearch(unittest.TestCase):

    def test_selection_sort(self):
        length = 100
        val_list = [i for i in range(length)]
        for i in range(10):
            x = randrange(0, length)
            self.assertEqual(val_list.index(x),
                             binary_search(val_list, 0, length - 1, x))


if __name__ == '__main__':
    unittest.main()
