"""
Radix Sort

- https://algorithm.yuanbin.me/zh-hans/basics_sorting/radix_sort.html
- https://www.geeksforgeeks.org/radix-sort/
"""

import unittest

from .util import generate_random_array
from .counting_sort import counting_sort
from functools import partial


def to_digit(elem, exp=1):
    """
    Return digit by given number and exp

    :param elem: given number
    :type elem: int
    :param exp: 10^i
    :type exp: int
    :return: digit
    :rtype: int
    """
    return (elem // exp) % 10


def radix_sort(array):
    """
    Sort array in ascending order by radix sort

    The idea of Radix Sort is to do digit by digit sort starting
    from least significant digit to most significant digit.
    Radix sort uses counting sort as a subroutine to sort.

    Counting sort is a linear time sorting algorithm that sort
    in O(n+k) time when elements are in range from 1 to k.
    What if the elements are in range from 1 to n^2? We can’t
    use counting sort because counting sort will take O(n^2)
    which is worse than comparison based sorting algorithms.
    Can we sort such an array in linear time? Radix Sort is
    the answer

    - Worst-case time performance: O(w * n)
    - Worst-case space complexity: O(w + n)

    where w is the number of bits required to store each key

    :param array: given unsorted array
    :type array: list
    :return: sorted array in ascending order
    :rtype: list
    """
    # find the maximum number to know number of digits
    max_val = max(array)
    # do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max_val // exp != 0:
        array = counting_sort(
            array,
            num_max=10,
            ord_func=partial(to_digit, exp=exp))
        exp *= 10

    return array


class TestRadixSort(unittest.TestCase):

    def test_radix_sort(self):
        val_list = generate_random_array()
        self.assertListEqual(sorted(val_list), radix_sort(val_list))


if __name__ == '__main__':
    unittest.main()
