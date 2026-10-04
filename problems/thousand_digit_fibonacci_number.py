# https://projecteuler.net/problem=25
# get the first/smallest fibonacci number to have 1000 digits

# Solving 2^a=10^1000 gives a~=3321, thats easily represented with a big int.
# the concern remains if the arithmatic of adding 2 massive numbers is tractable.
import math

lim = 10**999
# lim = 1000
i = 1
a = 1
b = 1
while(a < lim):
    c = b
    b += a
    a = c
    i += 1
    # if(a<20): print(f"{a}, {b}")
print(math.log10(a))
print(math.log10(b))
assert int(math.log10(a)) >= 999
print(i) # 4782