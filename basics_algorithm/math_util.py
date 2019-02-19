"""
Math Utilities

- https://algorithm.yuanbin.me/zh-hans/basics_algorithm/math/
"""

import unittest
import math
import random


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


def gcd(a, b):
    """
    Get greatest common divisor of given number a and b

    :param a: the first given number
    :type a: int
    :param b: the second given number
    :type b: int
    :return: greatest common divisor
    :rtype: int
    """
    return gcd(b, a % b) if b != 0 else a


def lcm(a, b):
    """
    Get least common multiple of given number a and b

    :param a: the first given number
    :type a: int
    :param b: the second given number
    :type b: int
    :return: least common multiple
    :rtype: int
    """
    return a * b // gcd(a, b)


def is_prime(n):
    """
    Check whether the given number is prime

    :param n: the given number
    :type n: int
    :return: whether the given number is prime
    :rtype: bool
    """
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return n > 1


def sieve(n):
    """
    Get prime numbers in the range of [0, n] by
    the sieve of Eratosthenes algorithm

    :param n: the given number
    :type n: int
    :return: list of prime numbers in the range of [0, n]
    :rtype: list[int]
    """
    prime_numebrs = []
    prime_flags = [True for _ in range(n)]
    prime_flags[0] = prime_flags[1] = False
    for i in range(n):
        if prime_flags[i] and is_prime(i):
            prime_numebrs.append(i)
            for j in range(0, n, i):
                prime_flags[j] = False
    return prime_numebrs


def sieve_range(lb, ub):
    """
    Get prime numbers in the range of [lb, ub] by
    the sieve of Eratosthenes algorithm

    :param lb: lower bound of range
    :type lb: int
    :param ub: upper bound of range
    :type ub: int
    :return: prime numbers in the range of [lb, ub]
    :rtype: list[int]
    """
    prime_numebrs = []
    prime_flags = [True for _ in range(ub)]
    prime_flags[0] = prime_flags[1] = False
    for i in range(ub):
        if prime_flags[i] and is_prime(i):
            if i >= lb:
                prime_numebrs.append(i)
            for j in range(0, ub, i):
                prime_flags[j] = False
    return prime_numebrs


class TestMathUtil(unittest.TestCase):

    def test_fast_pow_iterative(self):
        self.assertEqual(123 ** 10, fast_pow_iterative(123, 10))

    def test_fast_pow_recursive(self):
        self.assertEqual(1234 ** 100, fast_pow_recursive(1234, 100))
        self.assertEqual(2 ** -3, fast_pow_recursive(2, -3))
        self.assertAlmostEqual(2.5 ** 10, fast_pow_recursive(2.5, 10))

    def test_gcd(self):
        for _ in range(10):
            a = random.randint(0, 10000)
            b = random.randint(0, 10000)
            self.assertEqual(math.gcd(a, b), gcd(a, b))

    def test_lcm(self):
        for _ in range(10):
            a = random.randint(0, 10000)
            b = random.randint(0, 10000)
            self.assertEqual(a * b / math.gcd(a, b), lcm(a, b))

    def test_is_prime(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(10))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))

    def test_sieve(self):
        self.assertListEqual([2, 3, 5, 7, 11, 13, 17, 19], sieve(20))

    def test_sieve_range(self):
        self.assertListEqual([11, 13, 17, 19], sieve_range(10, 20))


if __name__ == '__main__':
    unittest.main()
