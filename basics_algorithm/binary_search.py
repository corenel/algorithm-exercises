"""
Binary Search

- https://algorithm.yuanbin.me/zh-hans/basics_algorithm/binary_search.html
- https://www.geeksforgeeks.org/binary-search/
"""

import unittest
from random import randrange


def binary_search_recursive(array, lb, ub, target):
    """
    Search target element in the given array by recursive binary search

    - Worst-case space complexity: O(n)
    - Worst-case performance: O(log n)

    :param array: given array
    :type array: list
    :param lb: index of lower bound
    :type lb: int
    :param ub: index of upper bound
    :type ub: int
    :param target: target element to search
    :type target: Any
    :return: index of target element, -1 for not found
    :rtype: int
    """
    # check base case
    if len(array) == 0 or ub < lb:
        return -1

    mid = lb + (ub - lb) // 2
    # if element is present at the middle itself
    if target == array[mid]:
        return mid
    # if element is larger than mid, then it
    # can only be present in right subarray
    elif target > array[mid]:
        return binary_search_recursive(array, mid + 1, ub, target)
    # else the element can only be present
    # in left subarray
    else:
        return binary_search_recursive(array, lb, mid - 1, target)


def binary_search_iterative(array, target):
    """
    Search target element in the given array by iterative binary search

    - Worst-case space complexity: O(1)
    - Worst-case performance: O(log n)

    :param array: given array
    :type array: list
    :param target: target element to search
    :type target: Any
    :return: index of target element, -1 for not found
    :rtype: int
    """
    # check base case
    if len(array) == 0:
        return -1
    # lower bound
    lb = 0
    # upper bound
    ub = len(array) - 1
    while lb <= ub:
        mid = lb + (ub - lb) // 2
        # if element is present at the middle itself
        if target == array[mid]:
            return mid
        # if element is greater than mid, then it
        # can only be present in right subarray
        elif target > array[mid]:
            lb = mid + 1
        # else the element can only be present
        # in left subarray
        else:
            ub = mid - 1
    return -1


def binary_search_lower_bound(array, target):
    """
    Search target element in the given array by iterative binary search

    - Worst-case space complexity: O(1)
    - Worst-case performance: O(log n)

    :param array: given array
    :type array: list
    :param target: target element to search
    :type target: Any
    :return: index of target element.
    :rtype: int
    """
    # check base case
    if len(array) == 0:
        return -1
    # lower bound
    lb = -1
    # upper bound
    ub = len(array)
    while lb + 1 < ub:
        mid = lb + (ub - lb) // 2
        # if element is greater than mid, then it
        # can only be present in right subarray
        if target > array[mid]:
            lb = mid
        # else the element can only be present
        # in left subarray
        else:
            ub = mid
    # array[index] >= target, min(index)
    return lb + 1 if lb != -1 else -1


def binary_search_upper_bound(array, x):
    """
    Search target element in the given array by binary search

    - Worst-case space complexity: O(1)
    - Worst-case performance: O(log n)

    :param array: given array
    :type array: list
    :param x: target element to search
    :type x: Any
    :return:  lower bound target element
    :rtype: int
    """
    # check base case
    if len(array) == 0:
        return -1
    # lower bound
    lb = -1
    # upper bound
    ub = len(array)
    while lb + 1 < ub:
        mid = lb + (ub - lb) // 2
        # if element is not less than mid, then it
        # can only be present in right subarray
        if x >= array[mid]:
            lb = mid
        # else the element can only be present
        # in left subarray
        else:
            ub = mid
    # array[index] <= target, max(index)
    return ub - 1


class TestBinarySearch(unittest.TestCase):

    def test_binary_search_recursive(self):
        length = 100
        val_list = [i for i in range(length)]
        for i in range(10):
            x = randrange(0, length)
            self.assertEqual(
                val_list.index(x),
                binary_search_recursive(val_list, 0, length - 1, x))

    def test_binary_search_iterative(self):
        length = 100
        val_list = [i for i in range(length)]
        for i in range(10):
            x = randrange(0, length)
            self.assertEqual(
                val_list.index(x),
                binary_search_iterative(val_list, x))

    def test_binary_search_lower_bound(self):
        # normal search
        length = 100
        val_list = [i for i in range(length)]
        for i in range(10):
            x = randrange(0, length)
            self.assertEqual(
                val_list.index(x),
                binary_search_lower_bound(val_list, x))
        # search duplicated number
        val_list = [1, 1, 2, 3, 4, 5, 6, 6, 7, 8, 9]
        self.assertEqual(6, binary_search_lower_bound(val_list, 6))
        self.assertEqual(11, binary_search_lower_bound(val_list, 10))
        self.assertEqual(-1, binary_search_lower_bound(val_list, 0))

    def test_binary_search_upper_bound(self):
        # normal search
        length = 100
        val_list = [i for i in range(length)]
        for i in range(10):
            x = randrange(0, length)
            self.assertEqual(
                val_list.index(x),
                binary_search_upper_bound(val_list, x))
        # search duplicated number
        val_list = [1, 1, 2, 3, 4, 5, 6, 6, 7, 8, 9]
        self.assertEqual(7, binary_search_upper_bound(val_list, 6))
        self.assertEqual(11, binary_search_lower_bound(val_list, 10))
        self.assertEqual(-1, binary_search_lower_bound(val_list, 0))


if __name__ == '__main__':
    unittest.main()
