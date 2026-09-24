# https://projecteuler.net/problem=53
import math

def toInt(x: list[int]) -> int:
    y = 0
    for i in reversed(range(len(x))):
        y += x[-i-1] * 10**i
    return y

amount = 1_000_000

total = 0
total_greater = 0
for n in range(1,100+1):
    for r in range(0,n+1):
        sum = math.comb(n,r)
        if sum > amount: total_greater += 1
        total += sum
print(total)
print(total_greater)