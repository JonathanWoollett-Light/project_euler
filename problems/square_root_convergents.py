# https://projecteuler.net/problem=57

# 1 / 2
# 1 /(2+(1 / 2)
# 1 /(2+ 1 /(2+1 / 2))
# 1 /(2+ 1 /(2+1 /(2+1/2)))

# 3/2
# 7/5
# 17/12
# 41/29
# 99/70

# Numerators
#   3     7    17    41    99
#      4    10    24    58
#         6    14    34
#            8    20
#               12

# Denominators
#   2     5    12    29    70
#      3     7    17    41
#         4    10    24
#            6    14
#               8

# the difference tables show
# d(k+1) = d(k) + n(k)
# n(k+1) = n(k) + 2·d(k)

import math

count = 0
n, d = 3,2
for _ in range(1_000):
    n, d = n + 2*d, n + d
    if int(math.log10(n)) > int(math.log10(d)):
        count += 1
print(count)