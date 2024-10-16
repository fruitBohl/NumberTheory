from sympy.ntheory import prime, totient


def fun(p, k):
    return p**k - p ** (k - 1)


if __name__ == "__main__":
    # for n in range(1,100):
    p = 3
    for k in range(1, 1000):
        print(f"p={p}, k={k}, {fun(p,k) % 3} mod 3")
