# https://projecteuler.net/problem=27
# for `n**2 + a*n + b` find the `a` and `b` which maximise the number of
# primes that can be reached by incrementing `n` starting from `n=0`.
# Restrict the search of `a` to `abs(a) < 1000` or `-1000 < a < 1000`
# Restrict the search of `b` to `abs(b) <= 1000` or `-1000 <= b <= 1000`

import math
from tqdm import tqdm

primes = [2]
prime_set = {1:0, 2:1}
max_test = 2

def isPrime(x: int):
    global max_test
    # print(f"x: {x} max_test:{max_test}")
    for i in range(max_test+1,x+1):
        lim = math.isqrt(i)
        is_prime = True
        for p in primes:
            if p > lim: break
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
            prime_set[i] = len(primes)
        max_test = i
    return x in prime_set


max_n = 0
max_a = None
max_b = None
f = lambda n,a,b: n**2 + a*n + b
# a very tractable range to brute force
with tqdm(total = 1999*(1999+2)) as pbar:
    for a in range(-1000+1,1000):
        for b in range(-1000,1000+1):
            n = 0
            while(isPrime(f(n,a,b))): n += 1

            if n > max_n:
                max_n = n
                max_a = a
                max_b = b
                pbar.set_description(f"n: {max_n}, a: {max_a}, b: {max_b}: {[f(n,max_a,max_b) for n in range(0,max_n)][:5]}")

            pbar.update()

print(max_a * max_b)