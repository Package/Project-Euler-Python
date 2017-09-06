from math import sqrt


def is_composite(num):
    if num < 3:
        return False

    for x in range(2, int(sqrt(num)) + 1):
        if num % x == 0:
            return True

    return False


def gen_composite(max_range):
    comp = []

    # No composites below 4
    for x in range(4, max_range + 1):
        if is_composite(x):
            comp.append(x)

    return comp

