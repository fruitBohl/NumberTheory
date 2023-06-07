from math import cos, floor, pi, sqrt, gcd

import pandas as pd
import plotly.graph_objects as go


def calculate_eigenvalue(n: int, j: int, k: int, l: int) -> tuple[float, float]:
    """
    Calculate both (+/- sqrt) eigenvalues of I(n,j,k) given l.
    """

    arg = (2 * pi * l) / n
    sqrt_component = sqrt((cos(arg * j) - cos(arg * k)) ** 2 + 1)

    return (
        cos(arg * j) + cos(arg * k) + sqrt_component,
        cos(arg * j) + cos(arg * k) - sqrt_component,
    )


def calculate_eigenvalues(n: int, j: int, k: int) -> list[float]:
    """
    Calculate an ordered list (from biggest to smallest) of all the eigenvalues of the graph
    I(n,j,k).
    """

    eigenvalues = []

    for l in range(n):
        (pos_eigenvalue, neg_eigenvalue) = calculate_eigenvalue(n, j, k, l)
        eigenvalues.append(pos_eigenvalue)
        eigenvalues.append(neg_eigenvalue)
    eigenvalues.sort(reverse=True)

    return eigenvalues


def calculate_energy(n: int, j: int, k: int) -> float:
    """
    Calculate the energy of I(n,j,k) where  n>=3, 1<=j<=k<n/2. This is just the sum
    of the absolute value of all eigenvalues of the I-Graph.
    """

    energy = 0

    for l in range(n):
        (pos_eigenvalue, neg_eigenvalue) = calculate_eigenvalue(n, j, k, l)
        energy += abs(pos_eigenvalue)
        energy += abs(neg_eigenvalue)

    return energy


def calculate_graph_with_smallest_second_eigenvalue(n: int) -> tuple[int, int]:
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
                ordered_eigenvalues = calculate_eigenvalues(n, j, k)

                if ordered_eigenvalues[1] < second_largest_eigenvalue:
                    second_largest_eigenvalue = ordered_eigenvalues[1]
                    final_j = j
                    final_k = k

    two_dimensional_eigenvalue_plot(n, final_j, final_k)

    return (n, final_j, final_k), second_largest_eigenvalue


def two_dimensional_eigenvalue_plot(n: int, j: int, k: int) -> None:
    """
    Plot all eigenvalues of the graph I(n,j,k)
    """

    data = []

    for l in range(n):
        (pos_eigenvalue, _) = calculate_eigenvalue(n, j, k, l)
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
            energy = calculate_energy(n, j, k)
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
                count += 1
                energies[k][j] = calculate_energy(n, j, k)

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
    fig.write_html(f"visualisations/`3d_energy_plot_{n}.html")


if __name__ == "__main__":
    pd.options.plotting.backend = "plotly"

    multiples_of_three = [3 * n for n in range(1, 51)]

    multiples_of_two = [2 * n for n in range(1, 51)]

    multiples_of_five = [5 * n for n in range(1, 51)]

    multiples_of_twelve = [12 * n for n in range(1, 32)]

    squares = [n * n for n in range(2, 51)]

    for n in multiples_of_twelve:
        print(calculate_graph_with_smallest_second_eigenvalue(n))

    # TODO: plot histogram of all different energies and amount of I-graphs which have
    # that corresponding energy

    # Some Conjectures:
    # 1. number of I-graphs in I(n,j,k) is the (floor(n / 2)/2)*(floor(n / 2)/2 - 1)/2
    #  triangular number if n is prime