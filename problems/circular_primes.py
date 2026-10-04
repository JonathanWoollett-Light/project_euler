# https://projecteuler.net/problem=35

# find all primes such that all rotations of their digits are prime

import math
from tqdm import tqdm
import bisect

primes = [2]
prime_set = set([1,2])

def isPrime(x: int):
    lim = math.isqrt(x)
    for p in primes:
        if p > lim: break
        if x % p == 0: return False
    primes.append(x)
    prime_set.add(x)
    return True

def toInt(x: list[int]) -> int:
    y = 0
    for i in reversed(range(len(x))):
        y += x[-i-1] * 10**i
    return y

def toList(x: int) -> list[int]:
    y = []
    for i in reversed(range(int(math.log10(x))+1)):
        y.append((x // 10**i) % 10)
    return y

# get all primes we might need, not efficient but it works
n = 1_000_000
for i in tqdm(range(3, n*10)): isPrime(i)
circular_primes = []

lim = bisect.bisect_left(primes, n)
with tqdm(total = lim, disable=False) as pbar:
    for p in primes[:lim]:
        base = toList(p)
        # print(f"{p}: ",end="")
        all_prime = True
        for offset in range(len(base)):
            rot = toInt(base[offset:] + base[:offset])
            # print(f"{rot} ",end="")
            if rot not in prime_set:
                all_prime = False
                break
        # print()
        if all_prime:
            circular_primes.append(p)
            pbar.set_description(f"{circular_primes[:5], circular_primes[-5:]}")
        pbar.update()
print(circular_primes)
print(len(circular_primes))