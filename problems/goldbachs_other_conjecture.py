# https://projecteuler.net/problem=46

# an odd composite is an odd number with 3 or more factors

# find the smallest odd composite which cannot be written as `p+2*a^b` where `p` is prime.

# so we should just iterate over all number n=1.. then in each case iterate through all primes less
# than n, then for each prime check `sqrt((n-p) / 2)` if its a whole number thats the valid square,
# if no squares can be found for any primes less than n, then thats the smallest odd composite that
# cannot be written as the sum of a prime and twice a square
import math

primes = [2]

def isPrime(x: int):
    lim = math.isqrt(x)
    for p in primes:
        if p > lim: break
        if x % p == 0: return False
    primes.append(x)
    return True

# checks that `x` is a composite number (e.g. has 3 or more factors)
def isComposite(x: int) -> bool:
    if x < 4: return False
    for d in range(2, math.isqrt(x) + 1):
        if x % d == 0: return True
    return False

i = 1
while(True):
    if isComposite(i):
        found = False
        # iterate through found primes
        j = 0
        while(j < len(primes) and primes[j] < i):
            if math.sqrt((i-primes[j]) / 2).is_integer():
                assert (i-primes[j]) % 2 == 0
                found = True
                break
            j += 1

        # iterate through new primes
        x = primes[-1] + 1
        while(not found and x < i):
            if isPrime(x):
                if math.sqrt((i-x) / 2).is_integer():
                    assert (i-x) % 2 == 0
                    found = True
            x += 1

        # if no valid prime with a respective square can be found, then this is the smallest odd
        # composite that doesn't meet the rule.
        if (not found):
            break

    # iterate next odd number
    i += 2
print(i)