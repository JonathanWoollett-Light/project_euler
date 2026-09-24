# find the sole arithmetic sequence, which consits of 3 4 digits prime numbers
# which are permutations of each other

import math
import bisect
from itertools import permutations

# a = [1,2,3,4,5]
# b = bisect.bisect_left(a,1)
# print(b)
# print(a[b])

primes = [2]

def isPrime(x: int):
    lim = math.isqrt(x)
    for p in primes:
        if p > lim: break
        if x % p == 0: return False
    primes.append(x)
    return True

steps = 3
digits = 4

# get all 4 digit primes
for i in range(3, 10**digits):
    isPrime(i)

n = bisect.bisect_left(primes,10**(digits-1))
fprimes = primes[n:]
print(fprimes[:10])
print(len(fprimes))
fprimes_set = set(fprimes)


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

assert toInt([1,2,3,4]) == 1234
assert toList(1234) == [1,2,3,4]

for i in range(0,len(fprimes)-steps):
    a_list = toList(fprimes[i])
    a = toInt(a_list)
    b_lists = list(permutations(a_list))
    b_set = set([toInt(b_list) for b_list in b_lists])
    for b_list in b_lists:
        b = toInt(b_list)
        step = b - a
        if step > 0 and b in fprimes_set:
            c = b + step
            if c in fprimes_set and c in b_set:
                print(f"found: {[a,b,c]} -> {toInt(a_list + list(b_list) + toList(c))}")
                print()

# why did it find `[2969, 6299, 9629]` twice?