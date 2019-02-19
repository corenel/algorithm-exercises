"""
Shuffle
---

Given an array, write a program to generate a random permutation of array
elements. This question is also asked as “shuffle a deck of cards” or
“randomize a given array”. Here shuffle means that every permutation of
array element should equally likely.

- https://algorithm.yuanbin.me/zh-hans/basics_algorithm/probability/shuffle.html
- https://www.geeksforgeeks.org/shuffle-a-given-array-using-fisher-yates-shuffle-algorithm/

Reservoir Sampling
---
Reservoir sampling is a family of randomized algorithms for randomly choosing
k samples from a list of n items, where n is either a very large or unknown
number. Typically n is large enough that the list doesn’t fit into main
memory. For example, a list of search queries in Google and Facebook.

So we are given a big array (or stream) of numbers (to simplify), and we need
to write an efficient function to randomly select k numbers where 1 <= k <= n.
Let the input array be stream[].

- https://www.geeksforgeeks.org/reservoir-sampling/
"""

import unittest
import random


def shuffle(array):
    """
    Generate a random permutation of the input array by Fisher–Yates
    shuffle algorithm

    The idea is to start from the last element, swap it with a randomly
    selected element from the whole array (including last). Now consider
    the array from 0 to n-2 (size reduced by 1), and repeat the process
    till we hit the first element.

    Time Complexity: O(n), assuming that the function rand() takes O(1) time.

    :param array: input array
    :type array: list
    :return: shuffled array
    :rtype: list
    """
    # start from the last element and swap one by one. We don't
    # need to run for the first element that's why i > 0
    for i in range(len(array) - 1, 0, -1):
        # pick a random index from 0 to i
        rand = random.randint(0, i + 1)
        # swap array[i] with the element at random index
        array[i], array[rand] = array[rand], array[i]
    return array


def reservoir_sample(array, n, k):
    """
    A function to randomly select k items from array[0..n-1].

    It can be solved in O(n) time. The solution also suits well for input
    in the form of stream. Following are the steps.

    1. Create an array reservoir[0..k-1] and copy first k items of
       stream[] to it.
    2. Now one by one consider all items from (k+1)th item to nth item.
        a.rGenerate a random number from 0 to i where i is index of current
           item in stream[]. Let the generated random number is j.
        b. If j is in range 0 to k-1, replace reservoir[j] with arr[i]

    Time Complexity: O(n)

    :param array: input array
    :type array: list
    :param n: sampling range
    :type n: int
    :param k: number of elements to sample
    :type k: int
    :return: sampled array
    :rtype: list
    """
    reservior = array[:k]
    idx = k
    while idx < n:
        rand = random.randint(0, idx + 1)
        if rand < k:
            reservior[rand] = array[idx]
        idx += 1
    return reservior


class TestShuffle(unittest.TestCase):
    def test_shuffle(self):
        length = 10
        val_list = [i for i in range(length)]
        print('Shuffled array: ', shuffle(val_list))

    def test_sample(self):
        length = 20
        val_list = [i for i in range(length)]
        print('Sampled array: ', reservoir_sample(val_list, 20, 10))


if __name__ == '__main__':
    unittest.main()
