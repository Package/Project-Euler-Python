from math import *

# Todo: finish this

def is_prime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False

    for y in range(3, ceil(sqrt(x)) + 1, 2):
        if x % y == 0:
            return False

    return True


def gen_primes():
    return [2] + [x for x in range(3, 1000000, 2) if is_prime(x)]



# def longest_prime_list(max_range):
#     curr_primes = [x for x in primes if x < max_range]
#     best_prime = 0
#     best_length = 0
#
#     for index, prime in enumerate(curr_primes):
#         curr_sum = 0
#         curr_len = 0
#
#         for x in range(0, index):
#             curr_sum += curr_primes[x]
#             curr_len += 1
#
#             if curr_sum < prime:
#                 continue
#             if curr_sum == prime:
#                 if curr_len >= best_length:
#                     best_length = curr_len
#                     best_prime = curr_primes[index]
#
#     print("Prime number {} has prime sequence sum length of {}".format(best_prime, best_length))


def longest_consecutive_prime(max_range):
    length = 0
    best_prime = 0
    prime = 0

    while primes[prime] < max_range:
        curr_sum = 0
        curr_len = 0

        for x in range(0, max_range):
            curr_sum += primes[x]
            curr_len += 1

            if curr_sum < primes[prime]:
                continue

            if curr_sum == primes[prime]:
                if curr_len > length:
                    best_prime = primes[prime]
                    length = curr_len
            else:
                print("{} had a length of {}".format(primes[prime], curr_len - 1))

        prime += 1

    print("Prime number {} with a consecutive length of {}.".format(best_prime, length))
    return best_prime

primes = gen_primes()
# longest_prime_list(1000)
longest_consecutive_prime(1000)
