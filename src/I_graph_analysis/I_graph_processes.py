from __future__ import annotations
from math import cos, sqrt, pi, comb, ceil, floor, prod, gcd
from itertools import combinations
from sympy import isprime
from sympy.ntheory import factorint
import networkx as nx
import matplotlib.pyplot as plt


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

    # def __del__(self):
    #     print(f"graph I({self.n},{self.j},{self.k}) deleted")

    def eigenvalue(self, l: int) -> tuple[float, float]:
        """
        Calculate both (+/- sqrt) eigenvalues of I(n,j,k) given l.
        """
        arg = (2 * pi * l) / self.n
        sqrt_component = sqrt((cos(arg * self.j) - cos(arg * self.k)) ** 2 + 1)

        return (
            cos(arg * self.j) + cos(arg * self.k) + sqrt_component,
            cos(arg * self.j) + cos(arg * self.k) - sqrt_component,
        )

    def eigenvalues(self) -> list[float]:
        """
        Calculate an ordered list (from biggest to smallest) of all the eigenvalues of the
        graph I(n,j,k).
        """
        eigenvalues = []

        for l in range(self.n):
            (pos_eigenvalue, neg_eigenvalue) = self.eigenvalue(l)
            eigenvalues.append(pos_eigenvalue)
            eigenvalues.append(neg_eigenvalue)
        eigenvalues.sort(reverse=True)

        return eigenvalues

    def energy(self) -> float:
        """
        Calculate the energy of I(n,j,k). This is just the sum of the absolute value
        of all eigenvalues of the I-Graph.
        """
        energy = 0

        for l in range(self.n):
            (pos_eigenvalue, neg_eigenvalue) = self.eigenvalue(l)
            energy += abs(pos_eigenvalue)
            energy += abs(neg_eigenvalue)

        return round(energy, 4)

    def generate_networkx_graph(self) -> nx.Graph:
        """
        Generates a Networkx form of the graph I(n,j,k). This graph has 2*n nodes with
        3*n edges.

        The nodes of the outer ring are 0 to n-1. and the edges of the inner
        ring are n to 2n - 1. Edges from (node, n + node), (node, j + node),
        (node, k + node)
        """

        G = nx.Graph()

        G.add_nodes_from(range(2 * self.n))

        for node in range(self.n):
            G.add_edge(node, self.n + node)
            G.add_edge(node, (self.j + node) % self.n)
            G.add_edge(self.n + node, self.n + (self.k + node) % self.n)

        return G

    def calculate_cheeger_constant(self, use_brute_force: bool = True) -> float:
        if use_brute_force:
            # get all possible subsets of vertices.
            vertex_subsets = []

            # find the corresponding edges which go from inside to outside each subset
            # leaving_edges_vertex_subsets = {vertex_subset: edge_list}
            leaving_edges_vertex_subsets = {}

            # find the minimum of the all these vals
            return min(leaving_edges_vertex_subsets)

        return 0

    def check_isomorphism(self, G: I_graph) -> bool:
        """
        Checks whether two I-graphs are isomorphic. From Wolfram Mathworld
        (https://mathworld.wolfram.com/IGraph.html) we have that two I-graphs I(n,j,k) and I(n,l,m)
        are isomorphic iff there exists an integer a relatively prime to n such that either
        {l, m}={aj (mod n), ak (mod n)} or {l, m}={aj (mod n), -ak (mod n)}

        Note: this function only checks isomorphism between two I-graphs.
        """

        n = self.n
        j = self.j
        k = self.k

        l = G.j
        m = G.k

        for a in range(1, n):
            if is_coprime(a, n):
                if (l == (a * j) % n and m == (a * k) % n) or (
                    l == (a * j) % n and m == (-a * k) % n
                ):
                    return True
        return False


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

    # def __del__(self):
    #     print(f"\nCollection of I-graphs with n={self.n} deleted")

    def count_collection(self, m: int = -1, use_brute_force: bool = False) -> int:
        """
        Counts the number of I-graphs in the collection,
        either using brute force, or the designed algorithm.

        # TODO: properly acount for isomorphism.
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
                        count += 1
                return count
            else:  # up to isomorphism graphs using algorithm
                choices = int(floor((n + 1) / 2))
                # if n % 2 == 1:
                #     choices += 1

                return comb(choices, 2)
        else:
            if use_brute_force:  # All graphs using brute force
                count = 0
                upper = floor(n / 2)

                if n % 2 == 1:
                    upper += 1

                for j in range(1, upper):
                    for k in range(1, upper):
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
        verbose: bool = False,
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
                        if verbose:
                            print(f"Brute force, {(n,j,k)}")
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

    def percentage_of_connected_graphs(self) -> int:
        connected_graphs = self.count_connected_graphs()

        return (self.count_connected_graphs() / self.count_collection()) * 100


if __name__ == "__main__":
    x = I_graph(5, 2, 2)
    G = x.generate_networkx_graph()
    nx.draw(G)
    plt.savefig("graph.png")
