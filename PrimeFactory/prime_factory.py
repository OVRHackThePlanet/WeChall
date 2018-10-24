# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 20:16:43 2018

@author: mfulghum
"""

import numpy as np

def sum_of_digits(num):
    return sum([int(char) for char in str(num)])

np.genfromtxt('primes1.txt', dtype=np.uint64)
primes = np.genfromtxt('primes1.txt', dtype=np.uint64).flatten()

primes_over_million = primes[primes > 1000000]

num_found = 0
idx = 0

while num_found < 2:
    if sum_of_digits(primes_over_million[idx]) in primes:
        print(primes_over_million[idx])
        num_found += 1
    idx += 1
    
# 1000033
# 1000037
# -> 10000331000037
