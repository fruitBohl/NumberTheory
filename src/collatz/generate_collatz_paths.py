#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 23:03:39 2023

@author: vcatt31
"""


# COLLATZ SEQUENCES
def collatz(paths: list[list[int]], num_iterations: int):
    if num_iterations == 0:
        print()

    else:
        paths = add_to_paths(paths)
        collatz(paths, num_iterations - 1)


def add_to_paths(paths: list[list[int]]):
    all_paths = []
    for path in paths:
        odd_path = path.copy()
        even_path = path.copy()

        even_path.append(path[-1] * 2)
        all_paths.append(even_path)
        print(even_path)

        if odd_path[-1] % 6 == 4 and odd_path[-1] > 4:
            odd_path.append(int((odd_path[-1] - 1) / 3))
            all_paths.append(odd_path)
            print(odd_path)

    return all_paths


collatz([[1]], 15)
