#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 18:40:20 2023

@author: vcatt31
"""

import math


# prime numbers smaller than n
def prime_numbers(n):
    primes = []
    for i in range(2, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i%j == 0:
                break
        else:
            primes.append(i)
    return primes

                
#  prime factorisation of a number n
def prime_factorisation(n):
    factors = []
    primes = prime_numbers(math.floor(n/2))
    for prime in primes:
        power = 0
        if n%prime == 0:
            while n%prime == 0:
                power += 1
                n = n/prime
            factors.append([prime, power])
    return(factors)


# mod reducing
# want to write n = a mod b so that b's are co-prime
def mod_reducing(a, b):
    a_s= []
    b_s = []
    factors = prime_factorisation(b)
    for factor in factors:
        b_s.append(factor[0]**factor[1])
        a_s.append(a  % factor[0]**factor[1])
    return([a_s, b_s])


# divide by two
def mod1(a):
     return([a[0]/2, a[1]/2])

#multiply by two
def mod2(a):
     return([2*a[0], 2*a[1]])

#multiply by 3 + 1
def mod3(a):
     return([3*a[0] + 1, 3*a[1]])
 
#minus 1 divide by 3
def mod4(a):
     return([(a[0]-1)/3, a[1]/3])    
 
#possible paths around max element of loop
#given x is the max element of a loop
#let us first find out what the possible moves are after x 
#the possible moves are 
    # div 2
    # multiply 3
    
def generate_binary_strings(bit_count):
    binary_strings = []
    def genbin(n, bs=''):
        if len(bs) == n:
            binary_strings.append(bs)
        else:
            genbin(n, bs + '0')
            genbin(n, bs + '1')


    genbin(bit_count)
    return binary_strings



num_steps = 6
num_paths = num_steps**2
possible_paths = generate_binary_strings(num_steps)

#steps following the maximum element
after_max_paths = []
for path in possible_paths:
    x = 1
    x_vals = []
    for step in range(num_steps):
        if path[step] == '0':
            x = x/2
        else:
            x = 3*x
        x_vals.append(x)
    if max(x_vals) < 1:
        after_max_paths.append(path)
print("After max paths = ", after_max_paths)

        
#steps preceding the maximum element
before_max_paths = []
for path in possible_paths:
    x = 1
    x_vals = []
    for step in range(num_steps):
        if path[step] == '0':
            x = x*2
        else:
            x = x/3
        x_vals.append(x)
    if max(x_vals) < 1:
        before_max_paths.append(path)
print("Before max paths = ", before_max_paths)


#steps following the minimum element
after_min_paths = []
for path in possible_paths:
    x = 1
    x_vals = []
    for step in range(num_steps):
        if path[step] == '0':
            x = x/2
        else:
            x = 3*x
        x_vals.append(x)
    if min(x_vals) > 1:
        after_min_paths.append(path)
print("After min paths = ", after_min_paths)
        
#steps preceding the minimum element
before_min_paths = []
for path in possible_paths:
    x = 1
    x_vals = []
    for step in range(num_steps):
        if path[step] == '0':
            x = x*2
        else:
            x = x/3
        x_vals.append(x)
    if min(x_vals) > 1:
        before_min_paths.append(path)
print("Before min paths = ", before_min_paths)


for path in after_max_paths:
    x = [4, 12]
    for step in path:
        if int(step == '0'):
            x = mod1(x)
        else:
            x = mod3(x)
        print(x)
            
            
    
    