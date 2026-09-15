# for a number to be divisible by 1..n,
# it only needs to be divisible by the largest multiples of
# each prime <n, e.g. for 10, it would be 9(3), 8(2), 7(7), 5(5)
import math

n = 20

# Gets primes <n
primes = []
for i in range(2, n + 1):
    if all(i % p != 0 for p in primes): primes.append(i)
print(primes)

# Multiply largest multiples of primes
total = 1
for p in primes:
    exp = int(math.log(n,p))
    total *= p ** exp
print(total)