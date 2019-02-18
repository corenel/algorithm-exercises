"""
Counting Sort

- https://algorithm.yuanbin.me/zh-hans/basics_sorting/bucket_sort.html
- https://www.geeksforgeeks.org/bucket-sort-2/
"""

import unittest

from .util import generate_random_string, generate_random_array


def to_idx(elem):
    """
    Convert element to index

    :param elem: element in the input array
    :type elem: int or str
    :return: corresponding index of given element
    :rtype: int
    """
    if isinstance(elem, str) and len(elem) == 1:
        return ord(elem)
    elif isinstance(elem, int):
        return elem
    else:
        raise NotImplementedError


def counting_sort(array, num_max=256, ord_func=to_idx):
    """
    Sort array in ascending order by counting sort

    Counting sort is a sorting technique based on keys between
    a specific range. It works by counting the number of objects
    having distinct key values (kind of hashing). Then doing some
    arithmetic to calculate the position of each object in the
    output sequence.

    - Worst-case time performance: O(n+k)
    - Worst-case space complexity: O(n+k)

    where k is the range of the non-negative key values

    :param array: given unsorted array
    :type array: list[str]
    :param num_max: maximum number of elements
    :type num_max: int
    :param ord_func: function to convert element into index
    :type ord_func: function
    :return: sorted array in ascending order
    :rtype: list[str]
    """

    # the output character array that will have sorted arr
    output = [None for _ in array]
    # create a count array to store count of individual
    # characters and initialize count array as 0
    count = [0 for _ in range(num_max)]

    # determine minimum value of input array
    min_val = ord_func(min(array))

    # store count of each character
    for char in array:
        count[ord_func(char) - min_val] += 1

    # change count[i] so that count[i] now contains actual
    # position of this character in output array
    for idx in range(1, len(count)):
        count[idx] += count[idx - 1]

    # build the output character array
    for idx in range(len(array)):
        output[count[ord_func(array[idx]) - min_val] - 1] = array[idx]
        count[ord_func(array[idx]) - min_val] -= 1

    return output[:len(array)]


class TestCountingSort(unittest.TestCase):

    def test_counting_sort_string(self):
        for length in range(50, 100):
            val_list = generate_random_string(length)
            self.assertListEqual(sorted(val_list), counting_sort(val_list))

    def test_counting_sort_integer(self):
        for length in range(10, 20):
            val_list = generate_random_array(length)
            self.assertListEqual(sorted(val_list), counting_sort(val_list))

    def test_counting_sort_negative_integer(self):
        for length in range(10, 20):
            val_list = generate_random_array(length) + [-e for e in generate_random_array(length)]
            self.assertListEqual(sorted(val_list), counting_sort(val_list))


if __name__ == '__main__':
    unittest.main()
