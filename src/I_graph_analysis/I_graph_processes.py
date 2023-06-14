from math import cos, sqrt, pi, comb, ceil, floor, prod, gcd
from itertools import combinations
from sympy import isprime
from sympy.ntheory import factorint


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


def num_connected_I_graphs_brute_force(n) -> int:
    """
    Brute force calculates the number of possible unique connected I-graphs with
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


def num_I_graphs(n: int) -> int:
    """
    Calculates the number of possible I-graphs (up to isomorphism)
    """

    return comb(int(ceil(n / 2) + 1), 2) - 1


def num_connected_I_graphs(n: int, subproblems: dict[int, int]) -> int:
    """
    Base Case: if n is a prime, simply return comb(int(ceil(p / 2) + 1), 2) - 1
    Recursive Case: loop over all factors of n and calculate the
                    sum for all factors f of (num_I_graphs_recursive(f))
                return comb(int(ceil(p / 2) + 1), 2) + sum(num_I_graphs_recursive(f)) - 1
    """

    if isprime(n):
        return comb(int(ceil(n / 2) + 1), 2) - 1

    subproblems_sum = 0
    prime_factors = factorint(n, multiple=True)

    for num in range(2, len(prime_factors)):
        for factor in set([prod(x) for x in combinations(prime_factors, num)]):
            if factor not in subproblems:
                subproblems[factor] = num_connected_I_graphs(factor, subproblems)
            subproblems_sum += subproblems[factor]

    for prime in factorint(n):
        if prime not in subproblems:
            subproblems[prime] = num_connected_I_graphs(prime, subproblems)
        subproblems_sum += subproblems[prime]

    return comb(int(ceil(n / 2) + 1), 2) - (subproblems_sum + 1)


def percentage_of_connected_I_graphs(n: int) -> int:
    """
    Gives the percentage of connected I-graphs for a particular n value
    """

    return (num_connected_I_graphs(n, {}) / num_I_graphs(n)) * 100
