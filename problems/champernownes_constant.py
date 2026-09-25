# https://projecteuler.net/problem=40
import math
from math import prod

def toList(x: int) -> list[int]:
    y = []
    for i in reversed(range(int(math.log10(x))+1)):
        y.append((x // 10**i) % 10)
    return y

digits = sorted([1,10,100, 1_000, 10_000, 100_000, 1_000_000])
print(f"digits: {digits}")

exp = 0
i = 1
found = []
while (digits):
    size = int(math.log10(i))
    
    next_exp = exp + 1 + size
    while digits and digits[0] > exp and digits[0] <= next_exp:
        y = toList(i)[digits[0]-exp-1]
        print(f"{digits[0]}th digit is {y}")
        found.append(y)
        digits.pop(0)

    exp = next_exp
    i += 1
print(found)
print(prod(found))