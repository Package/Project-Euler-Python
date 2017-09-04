

def check_pandigital(number, n):
    number = str(number)

    if len(number) is not n:
        return False

    for x in range(1, n + 1):
        if number.count(str(x)) is not 1:
            return False

    return True


def find_pandigital_products():
    pans = set()

    for x in range(1, 2500):
        for y in range(1, 2500):
            string = str(x) + str(y) + str(x * y)

            if len(string) is not 9:
                continue

            if check_pandigital(string, 9):
                pans.add(x*y)

    return sum(pans)

print(find_pandigital_products())
