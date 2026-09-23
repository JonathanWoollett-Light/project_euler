# https://projecteuler.net/problem=37
import math
from tqdm import tqdm

primes = [2]
primes_set = set([2])

def isPrime(x: int):
    lim = math.isqrt(x)
    for p in primes:
        if p > lim: break
        if x % p == 0: return False
    primes.append(x)
    primes_set.add(x)
    return True

def isTruncatablePrime(x):
    lhs = x
    rhs = x
    if x == 3797: print(f"lhs: {lhs}, rhs: {rhs}")

    tens = int(math.log10(x))
    for i in range(tens):
        lhs %= 10**(tens-i)
        rhs //= 10
        if x == 3797: print(f"lhs: {lhs} ({tens-i}), rhs: {rhs}")
        if lhs not in primes_set: return False
        if rhs not in primes_set: return False
    return True

truncable_primes = []
i = 3
with tqdm() as pbar:
    while len(truncable_primes) < 11:
        if isPrime(i) and i > 9:
            if isTruncatablePrime(i):
                truncable_primes.append(i)
                pbar.set_description(f"{truncable_primes}")
        i += 1
        pbar.update(1)

print(primes[:30])
print(truncable_primes)
print(sum(truncable_primes))