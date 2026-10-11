# https://projecteuler.net/problem=38

# A pandigital number of a number which contains every digit 1-9 once.
# Whats the largest `n` such that multiples of `n` (starting from 1, and not ending at 1) can be
# concatenated to be pandigital?

from itertools import permutations

# could loop over all numbers (which is essentially all permutations including duplicates)
# multiplying them and checking if the multiple has duplicate or 0
# or could you loop over all pandigitals, then test if the digits 0..n equal digits n+1..m times two


# e.g. `[1,9,2] * 2 = [3,8,4]`
# y > 0 and x > 0
def mulList(x: list[int], y: int) -> list[int]:
    z = []
    carry = 0
    for d in reversed(x):
        carry += d * y
        z.append(carry % 10)
        carry //= 10
    while carry > 0:
        z.append(carry % 10)
        carry //= 10
    return z[::-1]

def search(base: list[int], multiplier: int, x: list[int]) -> bool:
    y = mulList(base, multiplier)
    n = len(y)
    if y != x[:n]: return False
    if len(x[n:]) == 0: return True
    return search(base, multiplier+1, x[n:])

def toInt(x: list[int]) -> int:
    y = 0
    for i in reversed(range(len(x))):
        y += x[-i-1] * 10**i
    return y


lim = [9,8,7,6,5,4,3,2,1]
largest = 0
for a in permutations(lim):
    a = list(a)
    for i in range(1, 6):
        if search(a[:i],2,a[i:]):
            largest = max(largest, toInt(a))
print(largest)