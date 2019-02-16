"""
Bubble Sort

https://algorithm.yuanbin.me/zh-hans/basics_sorting/bubble_sort.html
"""

import unittest
from random import shuffle


def bubble_sort(array):
    """
    Sort array in ascending order by bubble sort

    Avg Time: O(n^2)
    Worst Time: O(n^2)
    Space: O(1)

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
        val_list = [i for i in range(10)]
        shuffle(val_list)
        self.assertListEqual(sorted(val_list), bubble_sort(val_list))


if __name__ == '__main__':
    unittest.main()
