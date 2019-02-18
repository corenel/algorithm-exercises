"""
Counting Sort

- https://algorithm.yuanbin.me/zh-hans/basics_sorting/bucket_sort.html
- https://www.geeksforgeeks.org/bucket-sort-2/
"""

import unittest

from .util import generate_random_string


def counting_sort(array, num_max=256):
    """
    Sort array in ascending order by counting sort

    Counting sort is a sorting technique based on keys between
    a specific range. It works by counting the number of objects
    having distinct key values (kind of hashing). Then doing some
    arithmetic to calculate the position of each object in the
    output sequence.

    - Worst-case time performance: O(n+k)
    - Worst-case space complexity: O(n+k)

    :param array: given unsorted array
    :type array: list[str]
    :param num_max: maximum number of elements
    :type num_max: int
    :return: sorted array in ascending order
    :rtype: list[str]
    """
    # the output character array that will have sorted arr
    output = ['' for _ in range(num_max)]
    # create a count array to store count of individual
    # characters and initialize count array as 0
    count = [0 for _ in range(num_max)]

    # store count of each character
    for char in array:
        count[ord(char)] += 1

    # change count[i] so that count[i] now contains actual
    # position of this character in output array
    for idx in range(1, len(count)):
        count[idx] += count[idx - 1]

    # build the output character array
    for idx in range(len(array)):
        output[count[ord(array[idx])] - 1] = array[idx]
        count[ord(array[idx])] -= 1

    return output[:len(array)]


class TestCountingSort(unittest.TestCase):

    def test_counting_sort(self):
        for length in range(50, 100):
            val_list = generate_random_string(length)
            self.assertListEqual(sorted(val_list), counting_sort(val_list))


if __name__ == '__main__':
    unittest.main()
