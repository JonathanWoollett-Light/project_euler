# https://projecteuler.net/problem=3
from tqdm import tqdm

primes = [2]
factors = []
# n = 13195
n = 600_851_475_143

def isPrime(x):
    for p in primes:
        if x % p == 0: return False
    return True

current = 3
with tqdm() as pbar:
    while (current < n):
        if isPrime(current):
            primes.append(current)
            if n % current == 0:
                n /= current
                factors.append(current)
                pbar.set_description(f"factors: {factors}")
        current += 1
        pbar.total = n
        pbar.update(1)
        pbar.refresh()
factors.append(current)
print(factors)