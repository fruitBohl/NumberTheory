import sympy
import math


def conjecture_one(q: int, n: int):
    """
    This function will test the following conjecture:

    For all primes q and for all a = 1,2,...,q-1,
        r_n+1 < r_1 * r_2 * ... * r_n for all n >= 3
    where r_i is the ith prime that is congruent to a mod q.
    """

    for a in range(1, q):
        # Generate the first n primes that are congruent to a mod q.
        r = []
        r_count = 1

        while len(r) < n:
            p = sympy.ntheory.prime(r_count)

            if p % q == a % q:
                r.append(p)

            r_count += 1

        found = False
        r_nplus1 = -1

        while not found:
            p = sympy.ntheory.prime(r_count)

            if p % q == a % q:
                r_nplus1 = p
                found = True
            r_count += 1

        print(f"{math.prod(r)} < {r_nplus1}")


if __name__ == "__main__":
    prime = 1
    n = 10

    conjecture_one(prime, n)
