
def rand_prime_in_range(_min, _max):
    import random

    prime_list = []
    for n in range(_min, _max):
        isPrime = True

        for num in range(2, n):
            if n % num == 0:
                isPrime = False

        if isPrime:
            prime_list.append(n)
    return random.choice(prime_list)


def pgcd(a, b):
    while b:
        a, b = b, a % b
    return a
