# https://projecteuler.net/problem=63

# count the number of n-digit positive integers which are also n'th powers e.g. 16807 is 5 digits
# and equals 7^5

import math

count = 0
# since 10^b is the smallest number with b+1 digits, a^b < 10^b is required for a^b to have b
# digits, which limits the base to a <= 9 (the power b is not limited by this)
for a in range(1,10):
    # a^b has `floor(b*log10(a)) + 1` digits, and as a <= 9 this grows with slope log10(a) < 1
    # while the target b grows with slope 1, so once a^b has fewer than b digits it always will,
    # meaning the upper limit on the power is the largest b where `floor(b*log10(a)) + 1 >= b`
    # i.e. b <= 1/(1 - log10(a)), which is 21 for a=9
    for b in range(1, int(1/(1 - math.log10(a))) + 1):
        if len(str(a**b)) == b: count += 1
print(count)