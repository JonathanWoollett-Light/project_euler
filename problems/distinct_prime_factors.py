# https://projecteuler.net/problem=47

# Find the first 4 consecutive numbers that each have 4 distinct prime factors.
#
# wrong: Find the first 4 consecutive numbers where each has 4 prime factors and non
# share any of the prime factors. (impossible, 2 of any 4 consecutive numbers are even)
# wrong: Find the first 4 numbers that share no prime factors
primes = []

import math

def step(x: int):
    lim = math.isqrt(x)
    factors = []
    rem = x
    for p in primes:
        if p > lim: break
        if rem % p == 0:
            factors.append(p)
            while rem % p == 0: rem //= p
    # at most 1 prime factor can be larger than sqrt(x), it's whatever is left
    if rem > 1: factors.append(rem)
    if factors == [x]: primes.append(x)
    return factors

# there is a graph of numbers where each number points to a larger number it shares
# no prime factors with, how do you append to this graph?
# do you effectively check all leaf nodes for each new number to see if any of
# these leaves have overlapping prime factors then point all the leafs which don't to this new node?
#
# the thing that prevents cycles is lower numbers always pointing to larger
# numbers, otherwise there would be cycles, and you would essentially be constructing these graph
# until you find a `n` length cycle to find `n` number with disctint factors

# i've overcomplicated the problem and my definition was wrong, the missing part is `consecutive`
# this makes it much easier and basically means this graph dynamic can be completely skipped.


nums = [(1,[]),(2,step(2)),(3,step(3)),(4,step(4))]
i = nums[-1][0] + 1
while(not all(len(f) == 4 for _,f in nums)):
    nums.pop(0)
    nums.append((i, step(i)))
    i += 1
print(nums)