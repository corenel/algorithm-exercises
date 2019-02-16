"""
Insertion Sort

- https://algorithm.yuanbin.me/zh-hans/basics_sorting/insertion_sort.html
- https://www.geeksforgeeks.org/insertion-sort/
"""

import unittest

from .util import generate_random_array


def insertion_sort(array):
    """
    Sort array in ascending order by insertion sort

    Insertion sort iterates, consuming one input element
    each repetition, and growing a sorted output list.
    At each iteration, insertion sort removes one element
    from the input data, finds the location it belongs within
    the sorted list, and inserts it there. It repeats until
    no input elements remain.

    Best-case time performance: O(n)
    Worst-case time performance: O(n^2)
    Average time performance: O(n^2)
    Worst-case space complexity: O(n)

    :param array: given unsorted array
    :type array: list
    :return: sorted array in ascending order
    :rtype: list
    """
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        # Move elements of array[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position to reamin the
        # correct position for array[i]
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


class TestInsertionSort(unittest.TestCase):

    def test_insertion_sort(self):
        val_list = generate_random_array()
        self.assertListEqual(sorted(val_list), insertion_sort(val_list))


if __name__ == '__main__':
    unittest.main()
