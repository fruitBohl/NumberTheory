import networkx as nx
import matplotlib.pyplot as plt
from typing import *


def calculate_cheeger_constant() -> int:
    # Sets
    num_nodes = 5

    V = range(5)  # set of nodes
    E = [frozenset({v, (v + 1) % 5}) for v in V]  # set of edges
    G = [
        frozenset({v, (v + 1) % 5}) for v in V
    ]  # adjacency list representation of graph

    # A path is a sorted tuple of squares visited, plus the square we are up to
    DA = [{(frozenset({v}), v) for v in V}]
    for l in V[1:]:
        DA.append(set())
        for d in DA[l - 1]:
            for v in G(d[1]):
                if v not in d[0]:
                    DA[l].add((d[0] | {v}, v))

    P = set(p[0] for p in DA[V[-1]])

    Paths = [{(frozenset({s}), s) for s in S}]
    for t in T[1:]:
        Paths.append(set())
        for p in Paths[t - 1]:
            for s in Neighbours(p[1], nMax):
                if s not in p[0]:
                    Paths[t].add((p[0] | {s}, s))

    # Variables

    # Objective

    return


if __name__ == "__main__":
    calculate_cheeger_constant
