#%%Distribution of not necessarily consecutive prime gaps 

#
#import math
import pylab
from matplotlib import pyplot as plt


# CONSTANTS
M = 20000 #number of primes examined. 
#maybe need to download a large file of prime numbers. 

# FUNCTIONS

def prime_numbers(pn: int):
    p = []
    for i in range(2, pn + 1):
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            p.append(i)
    return p

def primorials(pn: int): 
    p = prime_numbers(pn)
    q = [2]
    for i in p[1:]:
        if max(q) < max(p):
            q.append(i*max(q))
    return(q)

primes_ = prime_numbers(M)
primos = primorials(M)

GAPS = {i:[] for i in primos}
for N in primes_: 
    GAPS_ = {i:0 for i in primos}
    primes = prime_numbers(N)
    for i in primes: 
        for j in primes[primes.index(i)+1:]:
            if j-i in primos:
                GAPS_[j-i] += 1
    for i in GAPS_:
        GAPS[i].append(GAPS_[i])

RATS = {i:[] for i in primos}
for i in range(len(primes)): 
    for gap in GAPS:
        if GAPS[gap][i] == 0:
            RATS[gap].append(0)
        else:
            RATS[gap].append(GAPS[2][i]/GAPS[gap][i])


COLS = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# for gap in GAPS:
#     col = COLS[list(GAPS.keys()).index(gap)]
#     for i in range(len(primes)):
#         if GAPS[gap][i] > 1:
#             y = GAPS[gap][i]
#             x = i
#             plt.scatter(x, y, c=col)
# plt.legend()
# plt.show()

for rat in RATS:
    col = COLS[list(RATS.keys()).index(rat)]
    for i in range(len(primes)):
        if RATS[rat][i] > 0:
            y = RATS[rat][i]
            x = i
            plt.scatter(x, y, c=col)
plt.ylim(0, 1.1)
plt.legend()
plt.show()
# %%
