"""
Bucket Sort

- https://algorithm.yuanbin.me/zh-hans/basics_sorting/bucket_sort.html - https://www.geeksforgeeks.org/bucket-sort-2/
"""

import unittest

from .insertion_sort import insertion_sort
from .util import generate_uniform_float


def bucket_sort(array, num_slot=10):
    """
    Sort array in ascending order by bucket sort

    1) Create n empty buckets (Or lists).
    2) Do following for every array element arr[i].
        - Insert arr[i] into bucket[n*array[i]]
    3) Sort individual buckets using insertion sort.
    4) Concatenate all sorted buckets.

    - Best-case time performance: O(n log n)
    - Worst-case time performance: O(n log n)
    - Average time performance: O(n log n)
    - Worst-case space complexity: O(1)

    :param array: given unsorted array
    :type array: list
    :param num_slot: number of slots
    :type num_slot: int
    :return: sorted array in ascending order
    :rtype: list
    """
    # initialize buckets
    buckets = [[] for _ in range(num_slot)]

    # put array elements in different buckets
    for e in array:
        buckets[int(num_slot * e)].append(e)

    # sort individual buckets
    for idx in range(num_slot):
        buckets[idx] = insertion_sort(buckets[idx])

    # concatenate the result
    idx = 0
    for bucket in buckets:
        for e in bucket:
            array[idx] = e
            idx += 1

    return array


class TestBucketSort(unittest.TestCase):

    def test_bucket_sort(self):
        val_list = generate_uniform_float()
        self.assertListEqual(sorted(val_list), bucket_sort(val_list))


if __name__ == '__main__':
    unittest.main()
