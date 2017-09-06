from math import ceil

factor_map = {}


def get_factors(num):
    if num in factor_map:
        return factor_map[num]

    factors = []
    for x in range(2, int(ceil(num / 2)) + 1):
        if num % x == 0:
            factors.append(x)

    factor_map[num] = factors
    print("Done {}".format(num))
    return factors


for x in range(2, 1000001):
    get_factors(x)

print(factor_map)
