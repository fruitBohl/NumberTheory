#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 22:58:19 2023

@author: vcatt31
"""
# test
# estimating the expected proportion of evens in a collatz sequence of length n
# will print this proportion

# sequence length
seq_len = 30  # this is the variable that you can change


def recursive(possible_paths: list[tuple[list[int], int]], sequence_length: int):
    if sequence_length == 1:
        exp_num_evens = []
        for path in possible_paths:
            exp_num_evens.append((seq_len - sum(path[0])) * path[1])
        print(
            f"Expected proportion of primes in all sequences of length {seq_len} = {sum(exp_num_evens)/seq_len}"
        )

    else:
        possible_paths = iterate(possible_paths)
        recursive(possible_paths, sequence_length - 1)


def iterate(possible_paths: list[tuple[list[int], int]]):
    all_paths = []
    for path, likelihood in possible_paths:
        odd_even_path = path.copy()
        odd_even_likelihood = likelihood

        even_odd_path = path.copy()
        even_odd_likelihood = likelihood

        even_even_path = path.copy()
        even_even_likelihood = likelihood

        if path[-1] == 1:
            odd_even_path.append(0)
            all_paths.append((odd_even_path, odd_even_likelihood))

        else:
            even_odd_path.append(1)
            even_odd_likelihood *= 1 / 3
            all_paths.append((even_odd_path, even_odd_likelihood))

            even_even_path.append(0)
            even_even_likelihood *= 2 / 3
            all_paths.append((even_even_path, even_even_likelihood))

    return all_paths


def main():
    recursive([([1], 1)], seq_len)


if __name__ == "__main__":
    main()
