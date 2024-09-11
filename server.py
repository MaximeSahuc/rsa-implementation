#!/bin/python3

#####################
# Fichier de Maxime #
#####################


from utils import (
    rand_prime_in_range,
    pgcd,
    calc_e,
    calc_d,
)


def main():
    print("---- Server ----")
    prime_min_range = 10
    prime_max_range = 40

    p = rand_prime_in_range(_min=prime_min_range, _max=prime_max_range)
    q = rand_prime_in_range(_min=prime_min_range, _max=prime_max_range)
    print(f"p: {p}")
    print(f"q: {q}")

    n = p * q
    print(f"n: {n}")

    phi_n = (p - 1) * ( q - 1 )
    print(f"phi(n): {phi_n}")

    e = calc_e(phi_n)
    print(f"e: {e}")

    d = calc_d(e, phi_n)
    print(f"d: {d}")

if __name__ == "__main__":
    main()


