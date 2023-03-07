#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 10:36:55 2022

@author: vcatt31
"""
from math import prod
import numpy as np
import itertools

def prime_numbers(n):
    primes = []
    for i in range(2, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i%j == 0:
                break
        else:
            primes.append(i)
    return primes

def which_mods(prime_list):
    final_mod_list = []
    for i in prime_list:
        temp_list = []
        for j in range(1,i-2):
            temp_list.append(j)
        temp_list.append(i-1)
        final_mod_list.append(temp_list)
    return final_mod_list


def inverse_modulo(n, mod):
    for i in range(1, mod+1):
        if (n*i)%mod == 1:
            return i

def chinese_remainder(mods, prime_list):
    n=len(mods)
    product_primes = prod(prime_list)
    initial_prods = []
    for i in prime_list:
        initial_prods.append(int((product_primes/i)%i))
    for j in range(0,n):
        if initial_prods[j] != 1:
            initial_prods[j] = inverse_modulo(initial_prods[j], prime_list[j])
    c_r = 0
    for k in range(0,n):
        c_r += int(mods[k]*product_primes/prime_list[k]*initial_prods[k])
    return c_r%product_primes


def main(prime):
    prime_list = prime_numbers(prime)
    n = len(prime_list)
    mods = which_mods(prime_list)
    product_primes = prod(prime_list)
    num_comb = 1
    
    
    for i in mods:
        num_comb *= len(i)
        
    mat = [p for p in itertools.product(*mods)]

    
    pre_twins = []
    for i in mat:
        pre_twins.append(chinese_remainder(i, prime_list))
    
    big_primes_list = prime_numbers(2*product_primes)
    
    twins = []
    for i in pre_twins:
        if i in big_primes_list and (i+2) in big_primes_list:
            twins.append(i)
            
    percentage_twins = (len(twins))/len(mat)
    
    print("total_from_cr = ", len(mat))
    print("num_twin =", len(twins))
    print("num not twin = ", len(mat)-len(twins))
    print("percentage_twins =", percentage_twins)
    print(pre_twins)
    print(twins)
    
    return

main(11)



