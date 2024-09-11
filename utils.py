
import random

def rand_prime_in_range(_min, _max):
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


def calc_e(phi_n):
    e_list = []
    for num in range(1, phi_n):
        if pgcd(num, phi_n) == 1:
            e_list.append(num)
    return random.choice(e_list)


def calc_d(e, phi_n):
    from egcd import egcd
    return egcd(e, phi_n)[1] % phi_n
