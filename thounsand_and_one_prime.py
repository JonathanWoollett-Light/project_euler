# https://projecteuler.net/problem=7
primes = []
n = 10_001

def isPrime(x):
    for p in primes:
        if x % p == 0: return False
    return True


current = 2
while (len(primes) < n):
    if isPrime(current): primes.append(current)
    current += 1
    # print(f"{current} {len(primes)}")
print(primes[n-1])