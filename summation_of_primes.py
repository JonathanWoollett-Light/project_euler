from tqdm import tqdm
import numpy as np

primes = np.array([2])
def isPrime(x):
    # if x > 10000:
    #     print()
    #     print(f"x % primes: {x % primes}")
    #     print()
    #     raise Exception("pause here")
    return np.all(x % primes)

i = 3
total = 1
step = 0
n = 2_000_000
# n = 10
for i in tqdm(range(3,n,2)):
    if isPrime(i):
        # print(f"primes: {primes}")
        primes = np.append(primes,i)
        # print(f"primes: {primes}, i: {i}")
        total += i
print(primes)
print(total + 1)


# 1 -> 3 -> 5 -> 7 -> 9 -> 11 -> 13 -> 15
# 1 -> 3 -> 5 -> 7 -> 11 -> 
# is there some pattern of steps that can be built up to take larger steps between primes?
# gaps between primes