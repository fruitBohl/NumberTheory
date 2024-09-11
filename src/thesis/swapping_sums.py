from __future__ import annotations
from math import cos, sqrt, pi, comb, ceil, floor, prod, gcd
from itertools import combinations
from sympy import isprime
from sympy.ntheory import factorint
import networkx as nx
import matplotlib.pyplot as plt
from sympy.ntheory.factor_ import totient


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n + 1):
        if i * i <= n and n % i == 0:
            return False
    return True


def mobius(N):
    if N == 1:
        return 1

    p = 0
    for i in range(1, N + 1):
        if N % i == 0 and isPrime(i):
            if N % (i * i) == 0:
                return 0
            else:
                # i occurs only once,
                # increase f
                p = p + 1

    if p % 2 != 0:
        return -1
    else:
        return 1


def sum_phi_std(n: int) -> int:
    return sum([totient(i) for i in range(1, n + 1)])


def sum_phi_diff1(n: int) -> int:
    """Euler phi function in summation notation"""

    phi_sum = sum(
        [
            m * sum(mobius(d) / d for d in [i for i in range(1, m + 1) if m % i == 0])
            for m in range(1, n + 1)
        ]
    )

    return int(phi_sum)


def sum_phi_diff2(n: int) -> int:
    """Euler phi function in summation notation"""

    phi_sum = sum(
        [
            mobius(m) * sum(d for d in [i for i in range(1, floor(n / m)+1)])
            for m in range(1, n + 1)
        ]
    )

    return int(phi_sum)


if __name__ == "__main__":
    print(sum_phi_std(10), sum_phi_diff1(10), sum_phi_diff2(10))
