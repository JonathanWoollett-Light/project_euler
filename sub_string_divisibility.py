# https://projecteuler.net/problem=43
# find the sum of all pandigital number where n-th sliding window of 3 digits
# is divisble by the n-th prime number

from tqdm import tqdm
import math

primes = [2]

def isPrime(x: int):
    lim = math.isqrt(x)
    for p in primes:
        if p > lim: break
        if x % p == 0: return False
    primes.append(x)
    return True

def isPandigital(x):
    for i in range(1,8):
        y = x[i] * 100 + x[i+1] * 10 + x[i+2]
        # if 1406357289 == toInt(x):
        #     print(f"x[i]: {x[i]}, x[i+1]: {x[i+1]}, x[i+2]: {x[i+2]}, y: {y} {primes[i-1]}")
        #     print(x)
        if y % primes[i-1] != 0: return False
    return True

def toInt(x: list[int]) -> int:
    y = 0
    for i in reversed(range(len(x))):
        y += x[-i-1] * 10**i
    return y

# pan-digital number have 10 digits, 7 windows (other than the 1st) thus we only
# need the first 7 prime numbers after 1
i = 3
while (len(primes) < 7):
    isPrime(i)
    i += 1
print(primes)
from itertools import permutations

pans = []
for i in tqdm(permutations([i for i in range(10)])):
    # if 1406357289 == toInt(i): print(f"\n\n hit this: {toInt(i)}\n\n")
    if isPandigital(i): pans.append(i)
pans = [toInt(x) for x in pans]
print(pans)
print(sum(pans))