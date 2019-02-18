import string
from random import shuffle, uniform, choice


def generate_random_array(length=10):
    """
    Generate random shuffled array in given length

    :param length: array size
    :type length: int
    :return: random shuffled array in given length
    :rtype: list
    """
    val_list = [i for i in range(length)]
    shuffle(val_list)
    return val_list


def generate_uniform_float(length=10):
    """
    Generate uniform distributed float array in given length

    :param length: array size
    :type length: int
    :return: uniform distributed float array in given length
    :rtype: list
    """
    return [uniform(0, 1) for _ in range(length)]


def generate_random_string(length=10):
    """
    Generate uniform distributed float array in given length

    :param length: array size
    :type length: int
    :return: uniform distributed float array in given length
    :rtype: list
    """

    return ''.join([choice(string.printable) for _ in range(length)])
