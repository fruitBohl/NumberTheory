from math import cos, pi, sqrt, floor


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


if __name__ == "__main__":
    n = 12

    for k in range(floor(n/2)+1):
        for j in range(k+1):
            print(f"energy for I({n},{j},{k}) = {calculate_energy(n, j, k)}")
