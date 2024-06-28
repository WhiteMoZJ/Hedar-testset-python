import math


def get_result(x):
    """Bohachevsky's function 1

    Args:
        x (list): list of input variables

    Returns:
        float: value of Bohachevsky's function
    """
    return x[0] ** 2 + 2 * x[1] ** 2 - 0.3 * math.cos(3 * math.pi * x[0]) - 0.4 * math.cos(4 * math.pi * x[1]) + 0.7
