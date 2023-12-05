# Searching for cocliques
# Want to find the biggest family of hamilton paths on Kn such that they pairwise
# intersect in paths of length at most 1
# Searching for counterexamples to some intersection theorems for graphs.

# INITIALISING

from gurobipy import *
import itertools
from itertools import permutations
import networkx as nx
from copy import deepcopy


def intersection(a: set[frozenset[int]], b: set[frozenset[int]]) -> int:
    naive_intersection = a.intersection(b)
    G = nx.from_edgelist(naive_intersection)

    connected_components = list(nx.connected_components(G))

    if len(connected_components) == 0:
        return 0

    return len(max(nx.connected_components(G), key=len)) - 1


N = 8  # number of vertices
P = map(
    nx.utils.pairwise,
    [list(x) for x in list(permutations([n for n in range(1, N + 1)]))],
)

H = []

print(f"P set created")

for h in P:
    set_h = {frozenset({a, b}) for a, b in h}
    reverse_set_h = set(frozenset({b, a}) for a, b in set_h)
    if reverse_set_h not in H:
        H.append(set_h)

print(f"H set created: len = {len(H)}")

golden_boy = {
    frozenset({4, 5}),
    frozenset({5, 3}),
    frozenset({3, 6}),
    frozenset({6, 2}),
    frozenset({2, 7}),
    frozenset({7, 1}),
    frozenset({1, 8}),
}
boy_2 = {
    frozenset({1, 2}),
    frozenset({2, 8}),
    frozenset({8, 3}),
    frozenset({3, 7}),
    frozenset({7, 4}),
    frozenset({4, 6}),
    frozenset({6, 5}),
}
boy_3 = {
    frozenset({2, 3}),
    frozenset({3, 1}),
    frozenset({1, 4}),
    frozenset({4, 8}),
    frozenset({8, 5}),
    frozenset({5, 7}),
    frozenset({7, 6}),
}
boy_4 = {
    frozenset({3, 4}),
    frozenset({4, 2}),
    frozenset({2, 5}),
    frozenset({5, 1}),
    frozenset({1, 6}),
    frozenset({6, 8}),
    frozenset({8, 7}),
}
H_reduced = []

for h in H:
    if (
        intersection(golden_boy, h) < 2
        and intersection(boy_2, h) < 2
        and intersection(boy_3, h) < 2
        and intersection(boy_4, h) < 2
    ):
        H_reduced.append(h)
H_reduced.append(golden_boy)
H_reduced.append(boy_2)
H_reduced.append(boy_3)
H_reduced.append(boy_4)

print(f"H reduced set created: len = {len(H_reduced)}")

m = Model("Hamilton Path Cocliques")

# 1 if path is in family 0 otherwise
X = {i: m.addVar(vtype=GRB.BINARY) for i in range(len(H_reduced))}

print("Variables Created")

# OBJECTIVE
m.setObjective(quicksum(X[i] for i in range(len(H_reduced))), GRB.MAXIMIZE)

print("Objective added")

# CONSTRAINTS

# fix X[0] to be 1
m.addConstr(X[len(H_reduced) - 1] == 1)
m.addConstr(X[len(H_reduced) - 2] == 1)
m.addConstr(X[len(H_reduced) - 3] == 1)
m.addConstr(X[len(H_reduced) - 4] == 1)

for i in range(len(H_reduced)):
    for j in range(i + 1, len(H_reduced)):
        if intersection(H_reduced[i], H_reduced[j]) >= 2:
            m.addConstr(X[i] + X[j] <= 1)

# fix one specific path to be in it

print("Constraints added")

m.optimize()


# OUTPUTS
D = {}

for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        D[(i, j)] = 0

print(f"Largest family according to gurobi is {m.ObjVal}")
print(f"Largest family is actually {N*(N-1)/2}")

for h in range(len(H_reduced)):
    if X[h].x == 1:
        print(H_reduced[h])
