from sympy.ntheory import primefactors, prime
from numpy import prod


def jordan_totient(n: int, k: int) -> int:
    prime_div_terms = [(1 - 1 / p**k) for p in primefactors(n)]
    out = int(n**k * prod(prime_div_terms))

    return out


def Nth_sequence_term(N: int, k: int) -> int:
    x = [jordan_totient(n, k) for n in range(1, N + 1)]

    # for y in x:
    #     print(y)

    return 1 + sum(x)


if __name__ == "__main__":
    k = 2

    for i in range(1, 10000):
        nth = Nth_sequence_term(i, k)
        nth_sqrt = nth**0.5


        print(nth, nth_sqrt)

    # n = 4
    # for k in range(1, 25):
    #     print(f"prime = {n}, k={k}, {jordan_totient(n, k)}")
    # print("\n")
