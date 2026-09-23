# https://projecteuler.net/problem=45
from tqdm import tqdm
import math

def triangular(n):
    return n * (n + 1) / 2

# x = n * (3 * n - 1) / 2
# n = 1.0 + math.sqrt(1.0+24.0*x) / 6.0
def isPentagonal(x):
    n = (1.0 + math.sqrt(1.0+24.0*x)) / 6.0
    return (n,n.is_integer())

# x = n * (2n - 1)
# 0 = 2n**2 - n - x
# n = 1.0+math.sqrt(1.0+4.0*2.0*x) / 4.0
def isHexagonal(x):
    n = (1.0+math.sqrt(1.0+4.0*2.0*x)) / 4.0
    return (n,n.is_integer())

# i = 0
i = 286
with tqdm() as pbar:
    while(True):
        x = triangular(i)
        _,a = isPentagonal(x)
        _,b = isHexagonal(x)
        # if i == 285:
        #     print("\n\n")
        #     print(f"{i} -> {x} {a} ({y}) {b} ({z})")

        #     print(1.0 + math.sqrt(1.0+24.0*x) / 6.0)
        #     print(1.0 + math.sqrt(1.0+4.0*2.0*x) / 4.0)
        #     print("\n\n")

        #     break
        if a and b:
            print(f"\n\n{a} {b}\n\n")
            break

        i += 1
        pbar.update(i)
print(i)
x = triangular(i)
print(int(x))
print(isPentagonal(x))
print(isHexagonal(x))