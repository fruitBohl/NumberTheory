import math as m


def determine_differences(max_n: int):
    """
    Function used to determine the average difference in the size of gaps between numbers
    n and 2n, and between n^2 and (n+1)^2.
    """

    difference_double = 0
    difference_squared = 0
    previous_square_number = 1
    denom = 0
    n = 0

    while n <= max_n:
        if n == int(m.floor(m.sqrt(n))) ** 2:
            difference_double += n
            difference_squared += n - previous_square_number
            previous_square_number = n
            denom += 1
        n += 1

    print(
        f"average difference between n and 2n up until {max_n}: ",
        difference_double / denom,
    )
    print(
        f"average difference between n^2 and (n+1)^2 up until {max_n}: ",
        difference_squared / denom,
    )
    print(
        "ratio between difference squared and difference doubled: ",
        difference_squared / difference_double,
    )
    print()


if __name__ == "__main__":
    lst = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]
    for x in lst:
        determine_differences(x)

# FIRST FEW RESULTS

# average difference between n and 2n up until 10:  3.5
# average difference between n^2 and (n+1)^2 up until 10:  2.0
# ratio between difference squared and difference doubled:  0.5714285714285714

# average difference between n and 2n up until 100:  35.0
# average difference between n^2 and (n+1)^2 up until 100:  9.0
# ratio between difference squared and difference doubled:  0.2571428571428571

# average difference between n and 2n up until 1000:  325.5
# average difference between n^2 and (n+1)^2 up until 1000:  30.0
# ratio between difference squared and difference doubled:  0.09216589861751152

# average difference between n and 2n up until 10000:  3350.0
# average difference between n^2 and (n+1)^2 up until 10000:  99.0
# ratio between difference squared and difference doubled:  0.02955223880597015

# average difference between n and 2n up until 100000:  33338.0
# average difference between n^2 and (n+1)^2 up until 100000:  315.0
# ratio between difference squared and difference doubled:  0.009448677185194073

# average difference between n and 2n up until 1000000:  333500.0
# average difference between n^2 and (n+1)^2 up until 1000000:  999.0
# ratio between difference squared and difference doubled:  0.0029955022488755622

# average difference between n and 2n up until 10000000:  3333275.0
# average difference between n^2 and (n+1)^2 up until 10000000:  3161.0
# ratio between difference squared and difference doubled:  0.0009483165955404219

# average difference between n and 2n up until 100000000:  33335000.0
# average difference between n^2 and (n+1)^2 up until 100000000:  9999.0
# ratio between difference squared and difference doubled:  0.00029995500224988753
