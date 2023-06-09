from math import cos, sqrt, pi, comb, ceil, floor
from itertools import combinations


def gcd(p: int, q: int) -> int:
    """
    If p,q > 0, this returns the gcd of these integers.
    """
    while q != 0:
        p, q = q, p % q
    return p


def is_coprime(x: int, y: int) -> bool:
    """
    Determines whether two numbers are coprime.
    """
    return gcd(x, y) == 1


def phi(x: int) -> int:
    """
    Euler phi function
    """
    if x == 1:
        return 1
    else:
        n = [y for y in range(1, x) if is_coprime(x, y)]
        return len(n)


def I_eigenvalue(n: int, j: int, k: int, l: int) -> tuple[float, float]:
    """
    Calculate both (+/- sqrt) eigenvalues of I(n,j,k) given l.
    """
    arg = (2 * pi * l) / n
    sqrt_component = sqrt((cos(arg * j) - cos(arg * k)) ** 2 + 1)

    return (
        cos(arg * j) + cos(arg * k) + sqrt_component,
        cos(arg * j) + cos(arg * k) - sqrt_component,
    )


def I_eigenvalues(n: int, j: int, k: int) -> list[float]:
    """
    Calculate an ordered list (from biggest to smallest) of all the eigenvalues of the
    graph I(n,j,k).
    """
    eigenvalues = []

    for l in range(n):
        (pos_eigenvalue, neg_eigenvalue) = I_eigenvalue(n, j, k, l)
        eigenvalues.append(pos_eigenvalue)
        eigenvalues.append(neg_eigenvalue)
    eigenvalues.sort(reverse=True)

    return eigenvalues


def I_energy(n: int, j: int, k: int) -> float:
    """
    Calculate the energy of I(n,j,k) where  n>=3, 1<=j<=k<n/2. This is just the sum
    of the absolute value of all eigenvalues of the I-Graph.
    """
    energy = 0

    for l in range(n):
        (pos_eigenvalue, neg_eigenvalue) = I_eigenvalue(n, j, k, l)
        energy += abs(pos_eigenvalue)
        energy += abs(neg_eigenvalue)

    return round(energy, 4)


def num_I_graphs_prime(p) -> int:
    """
    Number of I-graphs where n is a prime.
    """
    return comb(int(ceil(p / 2) + 1), 2) - 1


def num_I_graphs_prime_squared(n) -> int:
    """
    Number of I-graphs where n is a prime squared.
    """
    return num_I_graphs_prime(n) - num_I_graphs_prime(int(sqrt(n)))


def num_I_graphs_two_primes(p, q) -> int:
    """
    Number of I-graphs where n is the product of two primes.
    """
    return num_I_graphs_prime(p * q) - (num_I_graphs_prime(p) + num_I_graphs_prime(q))


def num_I_graphs_brute_force(n) -> int:
    """
    Brute force calculates the number of possible unique I-graphs with
    a particular n value.
    """
    count = 0

    if n % 2 == 0:
        for k in range(floor(n / 2)):
            for j in range(k + 1):
                if gcd(gcd(k, j), n) == 1:
                    count += 1
    else:
        for k in range(floor(n / 2) + 1):
            for j in range(k + 1):
                if gcd(gcd(k, j), n) == 1:
                    count += 1
    return count


def num_I_graphs_general(n_prime_decomp: list[tuple[int, int]]) -> int:
    """
    Returns the number of connected I-graphs given I(n,j,k). TODO: currently only works
    for numbers with a prime decomposition with all primes with power 1.
    """

    n = 1
    count = 0

    primes = []

    for p, a in n_prime_decomp:
        primes.append(p)
        n *= p**a
    count = num_I_graphs_prime(n)

    print(count)

    for num_to_choose in range(2, max(len(primes), 3)):
        for subset in combinations(primes, num_to_choose):
            n_sub = 1
            sub_count = 0
            for prime in subset:
                sub_count -= num_I_graphs_prime(prime)
                n_sub *= prime
            sub_count += num_I_graphs_prime(n_sub)

            count -= sub_count
            print(num_I_graphs_prime(n_sub), sub_count)

    for prime in primes:
        count -= num_I_graphs_prime(prime)
        print(num_I_graphs_prime(prime), count)

    return count
