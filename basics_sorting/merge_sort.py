"""
Merge Sort

- https://algorithm.yuanbin.me/zh-hans/basics_sorting/merge_sort.html
- https://www.geeksforgeeks.org/merge-sort/
"""

import unittest

from .util import generate_random_array


def merge_sort(array):
    """
    Sort array in ascending order by merge sort

    Merge Sort is a Divide and Conquer algorithm. Conceptually,
    a merge sort works as follows:

    1. Divide the unsorted list into n sub-lists, each containing
    one element (a list of one element is considered sorted).

    2. Repeatedly merge sub-lists to produce new sorted sub-lists
    until there is only one sublist remaining. This will be the
    sorted list.

    - Best-case time performance: O(n log n)
    - Worst-case time performance: O(n log n)
    - Average time performance: O(n log n)
    - Worst-case space complexity: O(n)

    :param array: given unsorted array
    :type array: list
    :return: sorted array in ascending order
    :rtype: list
    """
    if len(array) > 1:
        # divide array into two part and sort them separately
        mid = len(array) // 2
        left = merge_sort(array[:mid])
        right = merge_sort(array[mid:])

        i = j = k = 0
        # merge two sub-lists
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        # if left part has extra items, add them to merged array
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        # if right part has extra items, add them to merged array
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    return array


class TestMergeSort(unittest.TestCase):

    def test_insertion_sort(self):
        val_list = generate_random_array()
        self.assertListEqual(sorted(val_list), merge_sort(val_list))


if __name__ == '__main__':
    unittest.main()
