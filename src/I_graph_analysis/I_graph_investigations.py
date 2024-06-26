from math import floor, gcd, ceil
from I_graph_processes import I_graph, I_Graph_Collection
import pandas as pd
import plotly.graph_objects as go
from sympy.ntheory import primorial
from sympy import isprime


# Some Conjectures:
# 2. As n->infinity the energies for all possible I-graphs with n value
#    group around n*(3+1/30).


def I_energy_distribution(n: int) -> int:
    """
    Plot histogram of all different energies and amount of I-graphs which have
    that corresponding energy.
    """

    energy_counts = {}
    count = 0

    for k in range(floor(n / 2) + 1):
        for j in range(k + 1):
            if gcd(gcd(k, j), n) == 1:
                G = I_graph(n, j, k)
                count += 1
                energy = G.energy()
                if energy in energy_counts.keys():
                    energy_counts[energy] += 1
                else:
                    energy_counts[energy] = 1

    energy_counts_df = pd.DataFrame(
        [(energy, count) for energy, count in energy_counts.items()],
        columns=["energy", "count"],
    )

    fig = energy_counts_df.plot.scatter(
        y="count",
        x="energy",
        title=f"Distribution of Energies For I-Graphs With n={n}",
    )
    fig.write_html(f"visualisations/energy_dist_{n}.html")
    return count


def I_graph_with_smallest_second_eigenvalue(n: int) -> tuple[int, int]:
    """
    takes an 'n' value as an input an calculates the respective j and k values which
    correspond to the graph with the smallest, second largest eigenvalue.

    This function will also graph the eigenvalues of this graph.
    """

    final_j = 0
    final_k = 0
    second_largest_eigenvalue = 1e15

    for k in range(floor(n / 2) + 1):
        for j in range(k + 1):
            if gcd(gcd(k, j), n) == 1:
                G = I_graph(n, j, k)
                ordered_eigenvalues = G.eigenvalues()

                if ordered_eigenvalues[1] < second_largest_eigenvalue:
                    second_largest_eigenvalue = ordered_eigenvalues[1]
                    final_j = j
                    final_k = k

    G_final = I_graph(n, final_j, final_k)

    two_dimensional_eigenvalue_plot(G_final)

    return G_final, round(second_largest_eigenvalue, 4)


def two_dimensional_eigenvalue_plot(G: I_graph) -> None:
    """
    Plot all eigenvalues of the graph I(n,j,k)
    """

    data = []

    for l in range(n):
        (pos_eigenvalue, _) = G.eigenvalue(l)
        data.append([l, pos_eigenvalue])

    df = pd.DataFrame(columns=["l-value", "Eigenvalue"], data=data)

    fig = df.plot.line(
        x="l-value",
        y="Eigenvalue",
        title=f"Eigenvalues of I({n},{j},{k}) Evaluated at Positive Square Root",
    )
    fig.write_html(f"visualisations/eigenvalue_plot_{n}_{j}_{k}.html")


def two_dimensional_energy_plot(n: int) -> None:
    """
    Plot all possible I-graphs (n,j,k) given a value for n.
    """

    data = []

    for k in range(floor(n / 2) + 1):
        for j in range(k + 1):
            G = I_graph(n, j, k)
            energy = G.energy()
            data.append([f"({j},{k})", energy])

    df = pd.DataFrame(columns=["(j,k)", "Energy"], data=data)

    fig = df.plot.line(
        x="(j,k)",
        y="Energy",
        title=f"Energy of I({n},j,k) With All Possible (j,k) Values",
    )
    fig.update_layout(xaxis_type="category")
    fig.write_html(f"visualisations/energy_plot_{n}.html")


def three_dimensional_energy_plot(n: int) -> None:
    """
    3D surface plot of energies for I(n,j,k)
    """

    energies = [[0 for _ in range(floor(n / 2) + 1)] for _ in range(floor(n / 2) + 1)]
    energy_set = set()
    count = 0

    for k in range(floor(n / 2) + 1):
        for j in range(k + 1):
            if gcd(gcd(k, j), n) == 1:
                G = I_graph(n, j, k)
                count += 1
                energies[k][j] = G.energy()

    for k in range(floor(n / 2) + 1):
        for j in range(k + 1):
            energy_set.add(round(energies[k][j], 3))

    print(
        f"All possible energies of I({n},j,k)", energy_set, f"Size is {len(energy_set)}"
    )
    print(f"Number of I-graphs = {count}")

    fig = go.Figure(
        go.Surface(
            x=list(range(floor(n / 2) + 1)),
            y=list(range(floor(n / 2) + 1)),
            z=energies,
            cauto=False,
            cmin=2.25 * n,
            cmax=4.25 * n,
            colorscale="Rainbow",
        )
    )

    fig.update_layout(
        title=f"Energy of I({n},j,k) With All Possible (j,k) Values",
        scene=dict(
            zaxis=dict(range=[2.25 * n, 4.25 * n]),
            xaxis_title="j Value",
            yaxis_title="k Value",
            zaxis_title="Energy",
        ),
    )
    fig.write_html(f"visualisations/3d_energy_plot_{n}.html")


if __name__ == "__main__":
    pd.options.plotting.backend = "plotly"

    for n in range(3, 1000):
        if not isprime(n):
            continue

        G_collection = I_Graph_Collection(n)
        brute_force_connected = G_collection.count_connected_graphs(use_brute_force=True)
        connected = G_collection.count_connected_graphs()

        print(f"n = {n}, examine = {ceil(n/2)}, connected = {connected}")

        assert brute_force_connected == connected

    # what percentage of I-graphs are connected (up to isomorphism)?
    # define S(N) to be the total number of I-graphs with n <= N (up to isomorphism)
    # denote T(N) to count those I-graphs with n<=N that are connected.
    # Then we would take the limit of T(N)/S(N) as N -> infinity.
