import itertools as _itertools
from statistics import mode

def primelist(n):
    """Returns a list of all primes less than n."""
    if n <= 2:
        return []
    nums = [True]*(n - 2)
    for num in range(2, _rootp1(n)):
        for counter in _itertools.count(num):
            product = counter * num
            if product >= n:
                break
            nums[product - 2] = False
    return [index for index, val in enumerate(nums, 2) if val]

def _rootp1(n: float) -> int:
    """returns the truncated square root of n plus 1 for use in range"""
    return int(n**0.5) + 1

def non_consecutive_gaps(primes: list) -> list:
    gaps = []
    for i in range(0, len(primes)):
        for j in range(i+1, len(primes)):
            if i != j:
                gaps.append(abs(primes[i] - primes[j]))
    return gaps

def most_common(n: int) -> int:
    primes = primelist(n)
    gaps = non_consecutive_gaps(primes)
    gap = mode(gaps)
    return gap


def common_gaps(n: int) -> list:
    gaps = [0,0,0]
    for i in range(4, n+1):
        gaps.append(most_common(i))
    return gaps

def critical_points(n: int) -> list:
    critical_ns = []
    gaps = common_gaps(n)
    for i in range(0, len(gaps)-1
                   ):
        if gaps[i] != gaps[i+1]:
            critical_ns.append(i+1)
    return critical_ns

def critical_points_function():
    play_again = 'y'
    while play_again == 'y':
        n = int(float(input("Please enter an integer larger than 4: ")))
        print(critical_points(n))
        play_again = input("Would you like to play again y/n? ")
             


"""This works, it just takes a long time to copmute .....

from 4


to i 
"""
