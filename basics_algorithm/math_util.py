"""
Math Utilities

- https://algorithm.yuanbin.me/zh-hans/basics_algorithm/math/
"""

import unittest


def fast_pow_iterative(x, n, mod=None):
    """
    This method divides the power problem into sub-problems of size n/2
    and compute the sub-problems iteratively.

    - Time Complexity: O(log n)
    - Space Complexity: O(1)
    - Algorithmic Paradigm: Divide and conquer.

    :param x: given number
    :type x: int
    :param n: given exponential
    :type n: int
    :param mod: large number to avoid overflow
    :type mod: int
    :return: result of pow
    :rtype: int
    """
    if mod is not None:
        res = 1 % mod
        while n > 0:
            if (n & 1) != 0:
                res *= x % mod
            x *= x % mod
            n >>= 1
    else:
        # in python 3, since there is no longer a limit to
        # the value of integers, we don't need the `mod` argument
        res = 1
        while n > 0:
            if (n & 1) != 0:
                res *= x
            x *= x
            n >>= 1
    return res


def fast_pow_recursive(x, n):
    """
    This method divides the power problem into sub-problems of size n/2
    and compute the sub-problems recursively.

    This function support float x and negative n

    - Time Complexity: O(log n)
    - Space Complexity: O(n)
    - Algorithmic Paradigm: Divide and conquer.

    :param x: given number
    :type x: int or float
    :param n: given exponential
    :type n: int
    :return: result of pow
    :rtype: int
    """
    if n == 0:
        return 1
    tmp = fast_pow_recursive(x, int(n / 2))
    if n % 2 == 0:
        return tmp * tmp
    elif n > 0:
        return tmp * tmp * x
    else:
        return tmp * tmp / x


class TestMathUtil(unittest.TestCase):

    def test_fast_pow_iterative(self):
        self.assertEqual(123 ** 10, fast_pow_iterative(123, 10))

    def test_fast_pow_recursive(self):
        self.assertEqual(1234 ** 100, fast_pow_recursive(1234, 100))
        self.assertEqual(2 ** -3, fast_pow_recursive(2, -3))
        self.assertAlmostEqual(2.5 ** 10, fast_pow_recursive(2.5, 10))


if __name__ == '__main__':
    unittest.main()
