from random import shuffle


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
