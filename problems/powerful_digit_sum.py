# https://projecteuler.net/problem=56
# whats the maximum digit sum of a^b where a < 100 and b < 100

# where c = a^b, we are trying to maximise 
import math

dsum = lambda c: sum([(c // 10**i) % 10 for i in range(int(math.log10(c))+1)])

# print(dsum(1234))
# print(dsum(4321))
# print(dsum(11111))
# print(dsum(22222))

# well that was easy to brute force
max_dsum = 0
for a in range(1,100):
    for b in range(1,100):
        max_dsum = max(dsum(a**b),max_dsum)
print(max_dsum)