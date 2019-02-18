"""
Selection Sort

- https://algorithm.yuanbin.me/zh-hans/basics_sorting/selection_sort.html
- https://www.geeksforgeeks.org/selection-sort/
"""

import unittest

from .util import generate_random_array


def selection_sort(array):
    """
    Sort array in ascending order by selection sort

    The selection sort algorithm sorts an array by repeatedly
    finding the minimum element (considering ascending order)
    from unsorted part and putting it at the beginning.

    - Best-case time performance: O(n^2)
    - Worst-case time performance: O(n^2)
    - Average time performance: O(n^2)
    - Worst-case space complexity: O(1)

    :param array: given unsorted array
    :type array: list
    :return: sorted array in ascending order
    :rtype: list
    """
    # traverse through all array elements
    for i in range(len(array)):
        min_idx = i
        # find the minimum element in remaining
        # unsorted array
        for j in range(i + 1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        # swap the found minimum element with
        # the first element
        array[i], array[min_idx] = array[min_idx], array[i]
    return array


class TestSelectionSort(unittest.TestCase):

    def test_selection_sort(self):
        val_list = generate_random_array()
        self.assertListEqual(sorted(val_list), selection_sort(val_list))


if __name__ == '__main__':
    unittest.main()
