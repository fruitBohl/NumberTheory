import math as m


def determine_differences(max_n: int):
    """
    Function used to determine the average difference in the size of gaps between numbers
    n and 2n, and between n^2 and (n+1)^2.
    """

    difference_double = 0
    difference_squared = 0
    previous_perfect_square = 1
    n = max_n

    while n > 0:
        difference_double += n
        if n == m.floor(m.sqrt(n))**2:
            difference_squared += (n - previous_perfect_square)
            previous_perfect_square = n
        n -= 1

    print(f"average difference between n and 2n up until {max_n}: ", difference_double/max_n)
    print(f"average difference between n^2 and (n+1)^2 up until {max_n}: ", difference_squared/max_n)


if __name__ == "__main__":
    determine_differences(100)