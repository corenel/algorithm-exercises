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
                # increment index of smaller element
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


def two_way_quick_sort(array, low, high):
    """
    Sort array in ascending order by quick sort

    :param array: given unsorted array
    :type array: list
    :param low: starting index of array to sort
    :type low: int
    :param high: ending index of array to sort
    :type high: int
    :return: sorted array in ascending order
    :rtype: list
    """

    def two_way_partition(arr, l, h):
        """
        Partition both from left and right

        :param arr: iven unsorted array
        :type arr: list
        :param l: starting index of array to sort
        :type l: int
        :param h: ending index of array to sort
        :type h: int
        :return: index of correctly positioned pivot element
        :rtype: int
        """
        p = arr[h]
        i = l
        j = h - 1

        while True:
            while i < j and arr[i] < p:
                i += 1
            while i < j and arr[j] >= p:
                j -= 1
            if i >= j:
                break
            arr[i], arr[j] = arr[j], arr[i]

        if arr[i] > arr[h]:
            arr[i], arr[h] = arr[h], arr[i]
        else:
            i += 1

        return i

    if low < high:
        pivot = two_way_partition(array, low, high)
        two_way_quick_sort(array, low, pivot - 1)
        two_way_quick_sort(array, pivot + 1, high)

    return array


def three_way_quick_sort(array, low, high):
    """
    Sort array in ascending order by quick sort

    :param array: given unsorted array
    :type array: list
    :param low: starting index of array to sort
    :type low: int
    :param high: ending index of array to sort
    :type high: int
    :return: sorted array in ascending order
    :rtype: list
    """

    def three_way_partition(arr, l, h):
        """
        Partition both from left and right


        This function partitions arr[] in three parts
        - arr[l..i] contains all elements smaller than pivot
        - arr[i+1..j-1] contains all occurrences of pivot
        - arr[j..r] contains all elements greater than pivot

        :param arr: iven unsorted array
        :type arr: list
        :param l: starting index of array to sort
        :type l: int
        :param h: ending index of array to sort
        :type h: int
        :return: index of correctly positioned pivot element
        :rtype: int
        """
        p = arr[h]
        i = l
        j = h - 1
        u = l - 1
        v = h

        print(p)
        while True:
            print(arr[l:h + 1], i, j, u, v)

            # from left, find the first element greater than
            # or equal to v. This loop will definitely terminate
            # as v is last element
            while arr[i] < p:
                i += 1

            # from right, find the first element smaller than or
            # equal to v
            while arr[j] > p:
                j -= 1
                if j == l:
                    break

            # if i and j cross, then we are done
            if i >= j:
                break

            # swap, so that smaller goes on left greater goes on right
            arr[i], arr[j] = arr[j], arr[i]

            # move all same left occurrence of pivot to beginning of
            # array and keep count using p
            if arr[i] == p:
                print(arr[l:h + 1], i, j, u, v)
                u += 1
                arr[i], arr[u] = arr[u], arr[i]

            # move all same right occurrence of pivot to end of array
            # and keep count using q
            if arr[j] == p:
                print(arr[l:h + 1], i, j, u, v)
                v -= 1
                arr[j], arr[v] = arr[v], arr[j]

        # move pivot element to its correct index
        print(arr[l:h + 1], i, j, u, v)
        print('move pivot element to its correct index')
        arr[i], arr[h] = arr[h], arr[i]
        print(arr[l:h + 1], i, j, u, v)

        print('move same occurrences')
        # move all left same occurrences from beginning
        # to adjacent to arr[i]
        j = i - 1
        for k in range(l, u):
            print(arr[l:h + 1], i, j, u, v)
            arr[k], arr[j] = arr[j], arr[k]
            j -= 1

        # move all right same occurrences from end
        # to adjacent to arr[i]
        i = i + 1
        for k in range(h - 1, v, -1):
            print(arr[l:h + 1], i, j, u, v)
            arr[k], arr[i] = arr[i], arr[k]
            i += 1

        print('result')
        print(arr[l:h + 1], i, j, u, v)
        print('---')

        return i, j

    if low < high:
        pivot_high, pivot_low = three_way_partition(array, low, high)
        three_way_quick_sort(array, low, pivot_low)
        three_way_quick_sort(array, pivot_high, high)

    return array


class TestQuickSort(unittest.TestCase):

    def test_quick_sort_out_place(self):
        for length in range(10, 20):
            val_list = generate_random_array(length)
            self.assertListEqual(sorted(val_list), quick_sort_out_place(val_list))

    def test_quick_sort_in_place(self):
        for length in range(10, 20):
            val_list = generate_random_array(length)
            self.assertListEqual(sorted(val_list),
                                 quick_sort_in_place(val_list, 0, len(val_list) - 1))

    def test_two_way_quick_sort(self):
        for length in range(10, 11):
            val_list = generate_random_array(length)
            self.assertListEqual(sorted(val_list),
                                 two_way_quick_sort(val_list, 0, len(val_list) - 1))

    def test_three_way_quick_sort(self):
        for length in range(10, 20):
            val_list = generate_random_array(length) + generate_random_array(length // 2)
            self.assertListEqual(sorted(val_list),
                                 three_way_quick_sort(val_list, 0, len(val_list) - 1))


if __name__ == '__main__':
    unittest.main()
