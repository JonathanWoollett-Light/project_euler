# https://projecteuler.net/problem=12
# t_n = 1+2+..+n

# the factors of a number can be calculated by counting all permutations of exponents of its prime
# factors. if x = p1^e1 * p2^e2 * .. * pk^ek then each factor picks an exponent 0..ei for each pi,
# giving (e1+1)(e2+1)..(ek+1) factors.

from tqdm import tqdm

def numFactors(x: int) -> int:
    count = 1
    p = 2
    # loops over candidate factors p up to sqrt of what's left of x. composite p never divide since
    # their prime factors were already divided out, so only primes contribute
    while p * p <= x:
        e = 0
        # loops over each power of p dividing x, dividing it out and counting the exponent e
        while x % p == 0:
            x //= p
            e += 1
        count *= e + 1
        p += 1
    # anything left over is a single prime factor larger than sqrt of the original x
    if x > 1:
        count *= 2
    return count

n = 1
t = 1
with tqdm() as pbar:
    while numFactors(t) <= 500:
        n += 1
        t += n
        pbar.update()
print(t)
