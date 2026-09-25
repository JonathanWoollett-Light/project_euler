# https://projecteuler.net/problem=41

# a pan-digital number if a number which makes use of all digits 1-n, e.g. 1234
# is n=4 pandigital
# find the largest n prime

import math
from itertools import permutations
from tqdm import tqdm



def isPrimeAlone(x:int):
    lim = math.isqrt(x)
    for p in range(2,x):
        if p > lim: break
        if x % p == 0: return False
    return True

def toInt(x: list[int]) -> int:
    y = 0
    for i in reversed(range(len(x))):
        y += x[-i-1] * 10**i
    return y


# iterating over all pandigitals and then iterating over numbers up to sqrt of
# that pandigital to check if prime seems faster than iteratng over all primes
# up to the largest pandigital becuase:
# 987654321 * primes 3..sqrt(987654321) > permutations * 3..sqrt(perm)
print(f"{987654321} * p > {sum([math.perm(n) for n in range(2,10)])} * p")

# primes = [2]
# primes_set = set([])
# def isPrime(x: int):
#     lim = math.isqrt(x)
#     for p in primes:
#         if p > lim: break
#         if x % p == 0: return False
#     primes.append(x)
#     primes_set.add(x)
#     return True
# # construct list of primes up to 987654321 (largest pandigital number)
# for i in tqdm(range(3,987654321+1,2)):
#     isPrime(i)

# since iteration goes from largest to smallest, we only need to iterate downwards until we hit a prime
def search():
    for n in reversed(range(2,10)):
        with tqdm(total = math.perm(n)) as pbar:
            for perm in permutations(reversed([i for i in range(1,n+1)])):
                x = toInt(perm)
                if isPrimeAlone(x): return x
                pbar.update()
    # print(f"largest for n<={n}: {largest}")
print(search())