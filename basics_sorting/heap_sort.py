"""
Heap Sort

- https://algorithm.yuanbin.me/zh-hans/basics_sorting/heap_sort.html
- https://www.geeksforgeeks.org/heap-sort/
- https://algs4.cs.princeton.edu/24pq/
"""

import unittest

from .util import generate_random_array
from basics_data_structure.heap import MinHeap


def heap_sort(array):
    """
    Sort array in ascending order by heap sort

    Heap sort is a comparison based sorting technique based on
    Binary Heap data structure. It is similar to selection sort
    where we first find the maximum element and place the maximum
    element at the end. We repeat the same process for remaining
    element.

    - Best-case time performance: O(n log n)
    - Worst-case time performance: O(n log n)
    - Average time performance: O(n log n)
    - Worst-case space complexity: O(1)

    :param array: given unsorted array
    :type array: list
    :return: sorted array in ascending order
    :rtype: list
    """
    heap = MinHeap(array)
    array_sorted = []
    while len(heap) > 0:
        array_sorted.append(heap.pop())

    return array_sorted


class TestMergeSort(unittest.TestCase):

    def test_merge_sort(self):
        val_list = generate_random_array()
        self.assertListEqual(sorted(val_list), heap_sort(val_list))


if __name__ == '__main__':
    unittest.main()
