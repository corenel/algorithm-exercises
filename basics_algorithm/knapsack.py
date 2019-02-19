"""
===
Knapsack
===

- https://algorithm.yuanbin.me/zh-hans/basics_algorithm/knapsack.html
- https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

Classical Knapsack Problem
---
Given weights and values of n items, put these items in a knapsack of capacity
W to get the maximum total value in the knapsack. In other words, given two
integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights
associated with n items respectively. Also given an integer W which represents
knapsack capacity, find out the maximum value subset of val[] such that sum of
the weights of this subset is smaller than or equal to W. You cannot break an
item, either pick the complete item, or don’t pick it (0-1 property).

Unbounded Knapsack problem
---
Given a knapsack weight W and a set of n items with certain value val[i] and
weight wti, we need to calculate minimum amount that could make up this
quantity exactly. This is different from classical Knapsack problem, here we
are allowed to use unlimited number of instances of an item.
"""

import unittest


def knapsack_0_1_recursive(w, wt, vt, n):
    """
    A naive recursive implementation of 0-1 Knapsack Problem

    A simple solution for 0-1 knapsack problem  is to consider all subsets
    of items and calculate the total weight and value of all subsets.
    Consider the only subsets whose total weight is smaller than W. From
    all such subsets, pick the maximum value subset.

    To consider all subsets of items, there can be two cases for every
    item:

    1. the item is included in the optimal subset.
    2. not included in the optimal set.

    Therefore, the maximum value that can be obtained from n items is
    max of following two values.

    1. Maximum value obtained by n-1 items and W weight (excluding
       nth item).
    2. Value of nth item plus maximum value obtained by n-1 items and
       W minus weight of the nth item (including nth item).

    If weight of nth item is greater than W, then the nth item cannot
    be included and case 1 is the only possibility.

    It should be noted that the recursive version function computes the
    same sub-problems again and again. Time complexity of this naive
    recursive solution is exponential (2^n).

    :param w: total capacity
    :type w: int
    :param wt: weight of each element
    :type wt: list[int]
    :param vt: value of each element
    :type vt: list[int]
    :param n: number of elements
    :type n: int
    :return: the maximum value that can be put in a knapsack of capacity w
    :rtype: int
    """
    # base case
    if w == 0 or n == 0:
        return 0

    # if weight of the nth item is more than Knapsack of capacity
    # w, then this item cannot be included in the optimal solution
    if wt[n - 1] > w:
        return knapsack_0_1_recursive(w, wt, vt, n - 1)
    else:
        # return the maximum of two cases:
        # (1) nth item included
        # (2) not included
        # state transition equation:
        # dp[i][j] = max{dp[i-1][j], dp[i-1][j - w[i]] + v[i]}
        return max(
            vt[n - 1] + knapsack_0_1_recursive(w - wt[n - 1], wt, vt, n - 1),
            knapsack_0_1_recursive(w, wt, vt, n - 1))


def knapsack_0_1_dp(w, wt, vt, n):
    """
    A Dynamic Programming based solution for 0-1 Knapsack problem

    Since sub-problems are evaluated again, this problem has Overlapping
    Sub-problems property. So the 0-1 Knapsack problem has both properties
    of a dynamic programming problem. Like other typical Dynamic Programming
    (DP) problems, re-computations of same sub-problems can be avoided by
    constructing a temporary array dp[][] in bottom up manner.

    Time Complexity: O(n*w) where n is the number of items and w is the
    capacity of knapsack.

    :param w: total capacity
    :type w: int
    :param wt: weight of each element
    :type wt: list[int]
    :param vt: value of each element
    :type vt: list[int]
    :param n: number of elements
    :type n: int
    :return: the maximum value that can be put in a knapsack of capacity w
    :rtype: int
    """
    dp = [[0 for _ in range(w + 1)] for _ in range(n + 1)]

    # build table K[][] in bottom up manner
    for n_idx in range(n + 1):
        for w_idx in range(w + 1):
            if n_idx == 0 or w_idx == 0:
                dp[n_idx][w_idx] = 0
            elif wt[n_idx - 1] > w:
                dp[n_idx][w_idx] = dp[n_idx - 1][w_idx]
            else:
                dp[n_idx][w_idx] = max(
                    vt[n_idx - 1] + dp[n_idx - 1][w_idx - wt[n_idx - 1]],
                    dp[n_idx - 1][w_idx])

    return dp[n][w]


def get_knapsack_0_1_solution(w, wt, vt, n):
    """
    Print solution of 0-1 knapsack problem

    :param w: total capacity
    :type w: int
    :param wt: weight of each element
    :type wt: list[int]
    :param vt: value of each element
    :type vt: list[int]
    :param n: number of elements
    :type n: int
    :return: indices of items to achieve maximum value in capacity w
    :rtype: list[int]
    """
    dp = [[0 for _ in range(w + 1)] for _ in range(n + 1)]

    # build table K[][] in bottom up manner
    for n_idx in range(n + 1):
        for w_idx in range(w + 1):
            if n_idx == 0 or w_idx == 0:
                dp[n_idx][w_idx] = 0
            elif wt[n_idx - 1] > w:
                dp[n_idx][w_idx] = dp[n_idx - 1][w_idx]
            else:
                dp[n_idx][w_idx] = max(
                    vt[n_idx - 1] + dp[n_idx - 1][w_idx - wt[n_idx - 1]],
                    dp[n_idx - 1][w_idx])

    res = dp[n][w]
    solution = []
    w_idx = w
    for n_idx in range(n, 0, -1):
        if res <= 0:
            break
        elif res == dp[n_idx - 1][w_idx]:
            continue
        else:
            solution.append(n_idx - 1)
            res -= vt[n_idx - 1]
            w_idx -= wt[n_idx - 1]
    return solution


def knapsack_unbounded(w, wt, vt, n):
    """
    It's an unbounded knapsack problem as we can use 1 or more instances of
    any resource. A simple 1D array, say dp[W+1] can be used such that dp[i]
    stores the maximum value which can achieved using all items and i capacity
    of knapsack. Note that we use 1D array here which is different from
    classical knapsack where we used 2D array. Here number of items never
    changes. We always have all items available.

    We can recursively compute dp[] using below formula

    - dp[i] = 0
    - dp[i] = max(dp[i], dp[i-wt[j]] + val[j]

    where j varies from 0 to n-1 such that: wt[j] <= i

    :param w: total capacity
    :type w: int
    :param wt: weight of each element
    :type wt: list[int]
    :param vt: value of each element
    :type vt: list[int]
    :param n: number of elements
    :type n: int
    :return: the maximum value that can be put in a knapsack of capacity w
    :rtype: int
    """
    # dp[i] is going to store maximum value with knapsack capacity i
    dp = [0 for _ in range(w + 1)]
    # fill dp[] using above recursive formula
    for w_idx in range(w + 1):
        for n_idx in range(n):
            if wt[n_idx] <= w_idx:
                dp[w_idx] = max(dp[w_idx], dp[w_idx - wt[n_idx]] + vt[n_idx])
    return dp[w]


class TestKnapsack(unittest.TestCase):

    def test_knapsack_0_1_recursive(self):
        w = 50
        wt = [10, 20, 30]
        vt = [60, 100, 120]
        n = len(vt)
        self.assertEqual(220, knapsack_0_1_recursive(w, wt, vt, n))

    def test_knapsack_0_1_dp(self):
        w = 50
        wt = [10, 20, 30]
        vt = [60, 100, 120]
        n = len(vt)
        self.assertEqual(220, knapsack_0_1_dp(w, wt, vt, n))

    def test_get_knapsack_0_1_solution(self):
        w = 50
        wt = [10, 20, 30]
        vt = [60, 100, 120]
        n = len(vt)
        # print('item indices: ', sorted(get_knapsack_0_1_solution(w, wt, vt, n)))
        self.assertListEqual([2, 1], get_knapsack_0_1_solution(w, wt, vt, n))

    def test_knapsack_unbounded(self):
        w = 100
        wt = [5, 10, 15]
        vt = [10, 30, 20]
        n = len(vt)
        self.assertEqual(300, knapsack_unbounded(w, wt, vt, n))


if __name__ == '__main__':
    unittest.main()
