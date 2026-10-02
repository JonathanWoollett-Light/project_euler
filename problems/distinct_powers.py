# https://projecteuler.net/problem=29
# How many distinct values can be product from a**b where 2<=a<=100 and 2<=b<=100

# it seems like 102**2 is very tractable for brute force, the problem is that
# 100**100 is just too big to calculate in normal ints, even big ints couldn't
# contain a number that big

# lets think about factoring, every number has a unique set of prime factors, so
# if we iterate through all the possible combinations of prime factors under
# sqrt(100**100) we would traverse all the unique combinations (and possibly
# some outside the range). Is this a meaningful speedup? We certainly couldn't
# calculate all primes up to 100**100 anyway so I think this is a dead end.

# The distinct values you find will just be 2..100 to their various exponents
# Importantly here why do seqeuences with such large ranges of a and b have
# quiet low limits?

# It seems like starting at 2**2, we can just increment a and b such that we get
# the next smallest value and repeat which will iterate through all uniques
# i think I was over-thinking
# this may not work since you could end up with min values that are too large if
# I can't write some proof the values will be tractables small, but eh I don't
# need to prove it to run the code I can just hope it works

# this doesn't work since its jumpy, 2^3 < 3^2 but 2^4 < 3^3  and 2^4 will never'
# get covered if a increments on the first check
# thus i think you need to build the stack of checks and collapse it over time


# this is all stupid and still fails at the point we can never calculate 100^100
# so if we ever have to even test that it fails.

# Is there a way to compare if a^b = c^d without fully evaluating the numbers?'
# E.g. if a^b was 126^893 (a number too large to calculate in memory? Does it
# just becomes a matter of dividng each down by its factors or prime factors and
# comparing through these or does this even work? or is there a better way?

# okay I'm being stupid, 100**100 is completely easy to represent with big ints
# really had an ai ah hallucination looping moment on that, got a brain like
# gpt 3
from tqdm import tqdm

values = set([])
with tqdm(total=102**2) as pbar:
    for a in range(2,100+1):
        for b in range(2,100+1):
            values.add(a**b)
            pbar.update()
print(f"{len(values)}")
