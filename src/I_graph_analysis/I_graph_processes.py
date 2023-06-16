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


class I_graph:
    """
    I-graph of the form I(n,j,k) with n>=3, 1<=j,k<n/2
    """

    def __init__(self, n: int, j: int, k: int):
        self.n = n
        self.j = j
        self.k = k

        if (n < 3) or (j < 1) or (k < 1) or (j > int(n / 2)) or (j > int(n / 2)):
            raise ValueError

    def __del__(self):
        print(f"graph I({self.n},{self.j},{self.k}) deleted")

    def I_eigenvalue(self, l: int) -> tuple[float, float]:
        """
        Calculate both (+/- sqrt) eigenvalues of I(n,j,k) given l.
        """
        arg = (2 * pi * l) / self.n
        sqrt_component = sqrt((cos(arg * self.j) - cos(arg * self.k)) ** 2 + 1)

        return (
            cos(arg * self.j) + cos(arg * self.k) + sqrt_component,
            cos(arg * self.j) + cos(arg * self.k) - sqrt_component,
        )

    def I_eigenvalues(self) -> list[float]:
        """
        Calculate an ordered list (from biggest to smallest) of all the eigenvalues of the
        graph I(n,j,k).
        """
        eigenvalues = []

        for l in range(self.n):
            (pos_eigenvalue, neg_eigenvalue) = self.I_eigenvalue(l)
            eigenvalues.append(pos_eigenvalue)
            eigenvalues.append(neg_eigenvalue)
        eigenvalues.sort(reverse=True)

        return eigenvalues

    def I_energy(self) -> float:
        """
        Calculate the energy of I(n,j,k). This is just the sum of the absolute value
        of all eigenvalues of the I-Graph.
        """
        energy = 0

        for l in range(self.n):
            (pos_eigenvalue, neg_eigenvalue) = self.I_eigenvalue(l)
            energy += abs(pos_eigenvalue)
            energy += abs(neg_eigenvalue)

        return round(energy, 4)


class I_Graph_Collection:
    """
    A collection of I-graphs of the form I(n,j,k) with n>=3, 1<=j,k<n/2. User can
    specify whether graphs in this collection are unique up to isomorphism (this
    essential means that j<=k), or by their defining tuple.
    """

    def __init__(self, n: int, up_to_isomorphism: bool = True):
        self.n = n
        self.up_to_isomorphism = up_to_isomorphism

        if n < 3:
            raise ValueError

    def __del__(self):
        print(f"Collection of I-graphs with n={self.n} deleted")

    def count_collection(self, m: int = -1, use_brute_force: bool = False) -> int:
        """
        Counts the number of I-graphs in the collection, either using brute force, or
        the designed algorithm.
        """

        n = self.n
        if m != -1:
            n = m

        if self.up_to_isomorphism:
            if use_brute_force:  # up to isomorphism graphs using brute force
                count = 0
                upper = floor(n / 2)

                if n % 2 == 1:
                    upper += 1

                for j in range(1, upper):
                    for k in range(j, upper):
                        print((n, j, k))
                        count += 1
                return count
            else:  # up to isomorphism graphs using algorithm
                choices = int(floor(n / 2))
                if n % 2 == 1:
                    choices += 1

                return comb(choices, 2)
        else:
            if use_brute_force:  # All graphs using brute force
                count = 0
                upper = floor(n / 2)

                if n % 2 == 1:
                    upper += 1

                for j in range(1, upper):
                    for k in range(1, upper):
                        print((n, j, k))
                        count += 1

                return count
            else:  # All graphs using algorithm
                choices = int(floor(n / 2))
                if n % 2 == 0:
                    choices -= 1

                return choices**2

    def count_connected_graphs(
        self,
        m: int = -1,
        subproblems: dict[int, int] = {},
        use_brute_force: bool = False,
    ) -> int:
        """
        Counts the number of connected I-graphs in the collection, either using brute
        force, or the designed algorithm.
        """

        n = self.n
        if m != -1:
            n = m

        if use_brute_force:
            lower = 1
            count = 0
            upper = floor(n / 2)

            if n % 2 == 1:
                upper += 1

            for j in range(1, upper):
                if self.up_to_isomorphism:
                    lower = j
                for k in range(lower, upper):
                    if gcd(n, gcd(j, k)) == 1:
                        print((n, j, k))
                        count += 1
            return count
        else:
            if isprime(n):
                return self.count_collection(n)

            subproblems_sum = 0

            prime_factors = factorint(n, multiple=True)

            for num in range(2, len(prime_factors)):
                for factor in set([prod(x) for x in combinations(prime_factors, num)]):
                    if factor not in subproblems:
                        subproblems[factor] = self.count_connected_graphs(
                            factor, subproblems
                        )
                    subproblems_sum += subproblems[factor]

            for prime in factorint(n):
                if prime not in subproblems:
                    subproblems[prime] = self.count_connected_graphs(prime, subproblems)
                subproblems_sum += subproblems[prime]

            return self.count_collection(n) - subproblems_sum

    def percentage_of_connected_I_graphs(self) -> int:
        return (self.count_connected_graphs() / self.count_collection()) * 100


if __name__ == "__main__":
    x = I_Graph_Collection(9, up_to_isomorphism=True)
    y = I_Graph_Collection(9, up_to_isomorphism=False)
    print("CONNECTED GRAPHS UP TO ISOMORPHISM WITH N=10")
    print(x.count_connected_graphs(), x.count_connected_graphs(use_brute_force=True))
    print(
        "\nCONNECTED GRAPHS INCLUDING ONES WHICH ARE ISOMORPHIC TO EACHOTHER WITH N=10"
    )
    print(y.count_connected_graphs(), y.count_connected_graphs(use_brute_force=True))
