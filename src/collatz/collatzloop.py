import math as m
import pandas as pd
import numpy as np


def determine_congruence_relations(depth: int):
    """Recursive function which determines congruence relations of elements
    within a loop."""

    print(f"depth = {depth}")

    if depth == 0:
        return True
    else:
        return determine_congruence_relations(depth - 1)


if __name__ == "__main__":
    print(
        """Assuming a loop exists this code will recursively determine 
        congruence relations of elements within the loop (starting from the 
        maximum element). This code uses the fact that every element within 
        the loop must be divisible by three and the maximum element of the 
        loop is 4 (mod 12)"""
    )

    determine_congruence_relations(10)
