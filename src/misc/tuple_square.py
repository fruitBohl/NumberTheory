from gurobipy import *
from math import sqrt


def tuple_square(n: int, first_val: int):
    N = range(n)
    E = []
    for n in N:
        for k in N:
            if n > k:
                E.append((n, k))

    env = gurobipy.Env(empty=True)
    env.setParam("OutputFlag", 0)
    env.start()
    m = Model("tuple square solver", env=env)

    X = {n: m.addVar(vtype=GRB.INTEGER) for n in N}  # value of each node
    Y = {e: m.addVar(vtype=GRB.INTEGER) for e in E}  # value at each edge
    Z = {e: m.addVar(vtype=GRB.INTEGER) for e in E}  # square values

    # value at each edge is equal to the sum of the values at each corresponding node
    for e in E:
        m.addConstr(Y[e] == X[e[0]] + X[e[1]])

    for e in E:
        m.addConstr(Z[e] * Z[e] == Y[e])

    # all numbers must be non-zero
    for n in N:
        m.addConstr(X[n] >= 1)

    # all numbers must be distinct
    for n in N:
        for i in N:
            if n > i:
                m.addConstr(X[n] >= X[i] + 1)

    m.addConstr(X[0] == first_val)

    m.setParam("NonConvex", 2)
    m.optimize()

    for n in N:
        print(X[n].x)


if __name__ == "__main__":
    K = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]

    for k in K:
        tuple_square(n=3, first_val=k)
        print("")
