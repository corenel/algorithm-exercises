"""
Bubble Sort

- https://algorithm.yuanbin.me/zh-hans/basics_sorting/bubble_sort.html
- https://www.geeksforgeeks.org/bubble-sort/
"""

import unittest

from .util import generate_random_array


def bubble_sort(array):
    """
    Sort array in ascending order by bubble sort

    Bubble sort, sometimes referred to as sinking sort,
    is a simple sorting algorithm that repeatedly steps
    through the list, compares adjacent pairs and swaps
    them if they are in the wrong order.

    - Best-case time performance: O(n)
    - Worst-case time performance: O(n^2)
    - Average time performance: O(n^2)
    - Worst-case space complexity: O(1)

    :param array: given unsorted array
    :type array: list
    :return: sorted array in ascending order
    :rtype: list
    """
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


class TestBubbleSort(unittest.TestCase):

    def test_bubble_sort(self):
        val_list = generate_random_array()
        self.assertListEqual(sorted(val_list), bubble_sort(val_list))


if __name__ == '__main__':
    unittest.main()
