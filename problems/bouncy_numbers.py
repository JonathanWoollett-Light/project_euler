# https://projecteuler.net/problem=112

# a bouncy number is a number where for every pair of adjacent digits the right
# digit is equal or greater than the left digit e.g. 134468
# the inverse is called a decreasing number
# a digit which is neither is a bouncy number

# Find the smallest `n` such that exactly 99% of the numbers less than `n` are bouncy

# we can do this by counting up, and counting every number which is bouncy and
# stopping when `count * 100 >= n * 99` (avoiding division since this produces floating point error)
# we only check this on non-bouncy numbers then step back to the exact answer

import math
from tqdm import tqdm

def isBouncy(x: int) -> bool:
    return not isIncreasing(x) and not isDecreasing(x)

# `isIncreasing` and `isDecreasing` can be combined but its ugly and not needed
# for the constant time speedup it gives.
def isIncreasing(x: int) -> bool:
    rhs = x % 10
    for i in range(1, int(math.log10(x))+1):
        lhs = x // 10**i % 10
        # if the lhs is ever greater than the rhs then it can't be increasing
        if lhs > rhs: return False 
        rhs = lhs
    return True

def isDecreasing(x: int) -> bool:
    rhs = x % 10
    for i in range(1, int(math.log10(x))+1):
        lhs = x // 10**i % 10
        # if the lhs is every less than the rhs then it can't be decreasing
        if lhs < rhs: return False
        rhs = lhs
    return True

assert isIncreasing(134468)
assert isDecreasing(66420)
assert isBouncy(155349)

n, non_bouncy = 100, 99 # 1..99 are all non-bouncy, 100 is counted in the loop
with tqdm() as pbar:
    while(True):
        # since >99% of iterations `not isBouncy(n) == False` its faster to have
        # the block rarely trigger
        if not isBouncy(n):
            non_bouncy += 1
            bouncy = n - non_bouncy
            pbar.set_description(f"n: {n}, bouncy: {bouncy}, bouncy/n: {bouncy / n}")
            if (bouncy * 100 >= n * 99): break
            pbar.update(n - pbar.n)
        n += 1

# the proportion of bouncy numbers only increases on bouncy numbers, so by only
# checking on non-bouncy numbers `n` overshoots 99%. Every number between the
# previous non-bouncy number and `n` is bouncy, so across that range the
# non-bouncy count is fixed at `non_bouncy - 1`. Exactly 99% bouncy is exactly 1%
# non-bouncy, so the answer is where `(non_bouncy - 1) / answer == 1 / 100`
answer = 100 * (non_bouncy - 1)
assert answer < n
print(f"n: {answer}, non_bouncy: {non_bouncy - 1}, bouncy: {answer - (non_bouncy - 1)}")