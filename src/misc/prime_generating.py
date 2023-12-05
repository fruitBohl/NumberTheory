import pygraphviz as pgv
from sympy import primefactors
import matplotlib.pyplot as plt
from numpy import prod


def generate_prime_graph(p0: int, d: int, iterations: int = 30) -> pgv.AGraph:
    """
    Given an initial prime number p0 and a 'shift' d, recursively generate a graph of primes
    where each successive node is a prime number and is connected a previous prime if the
    successor can be found inthe list of primes in the unique prime factorization of
    p0p1p2...pn + d

    TODO: this currently only takes the first prime of the factorization, adjust this in
    the future
    """

    A = pgv.AGraph(directed=True)
    A.add_node(p0)

    previous_p = int(p0)

    while iterations != 0:
        x = prod([int(n) for n in A.nodes()]) + d
        i = 0
        factors = primefactors(x)

        # find first new prime in the factorization
        while factors[i] in [int(n) for n in A.nodes()]:
            i += 1

            if i == len(factors):
                print(
                    "something has gone horribly wrong (offset probs not relatively prime)"
                )
                return A

        # add the new prime to the graph (unless)
        A.add_node(factors[i])
        A.add_edge(previous_p, factors[i])

        previous_p = factors[i]
        iterations -= 1

    return A


if __name__ == "__main__":
    A = generate_prime_graph(2, 1)
    A.layout("dot")
    A.draw("graph.png")

    """
    Some things to investigate:
        1. which small primes are slow to show up in general (regardless of p0 and d)
        2. Are certain types of twin primes showing up more commonly than usual (twin primes etc)
        3. How much different is the number of primes less than n.

    Conjecture:
        1. Irrespective of p0 and d we will eventually generate all primes.
    """
