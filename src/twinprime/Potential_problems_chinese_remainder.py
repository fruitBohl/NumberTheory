#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 16:16:57 2022

@author: vcatt31
"""

from math import prod, sqrt
import numpy as np

def prime_numbers(n):
    primes = []
    for i in range(2, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i%j == 0:
                break
        else:
            primes.append(i)
    return primes

def primorial(n, prime_numbers):
    primorial_prod = 1
    for i in prime_numbers:
        if i <= n:
            primorial_prod *= i
    return primorial_prod
 
def main(n):
    
    smaller_primes = prime_numbers(n)
    primo = primorial(n, smaller_primes)
    bigger_primes = prime_numbers(int(primo/n))
    potential_problems = []
    
    for i in smaller_primes:
        bigger_primes.remove(i)
               
    
    for i in bigger_primes:
        for j in bigger_primes:
            if i*j < primo and [j, i] not in potential_problems:
                potential_problems.append([i,j])
    print("num_potential_problems =", len(potential_problems))
    return

main(11)