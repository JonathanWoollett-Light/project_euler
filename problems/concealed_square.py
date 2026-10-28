# https://projecteuler.net/problem=206

# Find the single unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0 where each _ represents any single digit
import math
from tqdm import tqdm

def checker(x: int) -> bool:
    # skip comparing the trailing 0
    return all((x // 10**i) % 10 == y for i,y in zip(range(0,17,2),reversed([1,2,3,4,5,6,7,8,9])))

assert checker(10203040506070809)

# There are 2 simple ways to approach this:
# 1. Iterate through every number between `math.isqrt(1020304050607080900)` and `math.isqrt(1929394959697989990)` which is 378,925,613 comparisons
# 2. Iterate through the product of possible numbers in the gaps 10**9

min = math.isqrt(1020304050607080900 // 100)
max = math.isqrt(1929394959697989990 // 100)
print(f"brute force range: {max-min}")

# if we just cover the shortened range, we can always assume there is a 0 at the end since this can be got by just x10
with tqdm(total=max-min) as pbar:
    for i in range(min,max):
        if checker(i**2):
            pbar.clear()
            print(f"\n\n{i*10}**2 = {(i*10)**2}\n\n")
            break
        pbar.update()
