from math import cos, pi, sqrt, floor
import pandas as pd
import numpy as np
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


def two_dimensional_plot(n: int) -> None:
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
    fig.write_html(f"energy_plot_{n}.html")


def three_dimensional_plot(n: int) -> None:
    """
    3D surface plot of energies for I(n,j,k)
    """

    energies = [[0 for _ in range(floor(n / 2) + 1)] for _ in range(floor(n / 2) + 1)]

    for k in range(floor(n / 2) + 1):
        for j in range(k + 1):
            energies[k][j] = calculate_energy(n, j, k)

    fig = go.Figure(
        go.Surface(
            contours={
                "x": {
                    "show": True,
                    "start": 1.5,
                    "end": 2,
                    "size": 0.04,
                    "color": "white",
                },
                "z": {"show": True, "start": 0.5, "end": 0.8, "size": 0.05},
            },
            x=list(range(floor(n / 2) + 1)),
            y=list(range(floor(n / 2) + 1)),
            z=energies,
        )
    )
    fig.write_html(f"3d_energy_plot_{n}.html")


if __name__ == "__main__":
    pd.options.plotting.backend = "plotly"
    three_dimensional_plot(50)
