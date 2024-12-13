from sympy.ntheory import factorint


def g1(n: int) -> int:
    factors = factorint(n)
    out = 1

    for p in factors.keys():
        out *= ((p + 1) * p ** factors[p] - 2) / (p - 1)

    return out


if __name__ == "__main__":
    for N in range(1, 1000000, 100000):
        g1_sum = sum(g1(n) for n in range(1, N))
        print(f"n = {N}, g1/N^2={g1_sum/N**2}")
