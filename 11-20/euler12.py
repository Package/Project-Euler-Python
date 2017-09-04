
def triangle_number(index):
    return sum(range(1, index+1))


def get_factors(number):
    factors = [1, number]

    for x in range(2, int(number / 2) + 1, 1):
        if number % x == 0:
            factors.append(x)

    return factors


def five_hundred_divisors():
    number = 1
    while True:
        if len(get_factors(triangle_number(number))) >= 200:
            return triangle_number(number)
        number += 1

print(five_hundred_divisors())