"""
Quick Sort

- https://algorithm.yuanbin.me/zh-hans/basics_sorting/quick_sort.html
- https://www.geeksforgeeks.org/quick-sort/
"""

import unittest

from .util import generate_random_array


def quick_sort_out_place(array):
    """
    Sort array in ascending order by quick sort

    :param array: given unsorted array
    :type array: list
    :return: sorted array in ascending order
    :rtype: list
    """
    if len(array) > 1:
        pivot = array[0]
        left = [x for x in array if x < pivot]
        right = [x for x in array if x > pivot]
        return quick_sort_out_place(left) + [pivot] + quick_sort_out_place(right)

    return array


def quick_sort_in_place(array, low, high):
    """
    Sort array in ascending order by quick sort

    - Best-case time performance: O(n log n)
    - Worst-case time performance: O(n^2)
    - Average time performance: O(n log n)
    - Worst-case space complexity: O(log n)

    :param array: given unsorted array
    :type array: list
    :param low: starting index of array to sort
    :type low: int
    :param high: ending index of array to sort
    :type high: int
    :return: sorted array in ascending order
    :rtype: list
    """

    def partition(arr, l, h):
        """
        This function takes last element as pivot, places
        the pivot element at its correct position in sorted
        array, and places all smaller (smaller than pivot)
        to left of pivot and all greater elements to right
        of pivot

        :param arr: iven unsorted array
        :type arr: list
        :param l: starting index of array to sort
        :type l: int
        :param h: ending index of array to sort
        :type h: int
        :return: index of correctly positioned pivot element
        :rtype: int
        """
        # index of pivot element
        pi = arr[h]
        # index of smaller element
        i = l - 1
        for j in range(l, h):
            # if current element is smaller than or
            # equal to pivot, exchange it with the
            # smaller element
            if arr[j] <= pi:
                i += 1
                arr[j], arr[i] = arr[i], arr[j]
        # put pivot element to its correct position
        arr[i + 1], arr[h] = arr[h], arr[i + 1]
        return i + 1

    if low < high:
        # pivot is partitioning index, array[pvot] is now
        # at right place
        pivot = partition(array, low, high)
        # separately sort elements before
        # partition and after partition
        quick_sort_in_place(array, low, pivot - 1)
        quick_sort_in_place(array, pivot + 1, high)

    return array


class TestQuickSort(unittest.TestCase):

    def test_quick_sort_out_place(self):
        val_list = generate_random_array()
        self.assertListEqual(sorted(val_list), quick_sort_out_place(val_list))

    def test_quick_sort_in_place(self):
        val_list = generate_random_array()
        self.assertListEqual(sorted(val_list),
                             quick_sort_in_place(val_list, 0, len(val_list) - 1))


if __name__ == '__main__':
    unittest.main()
