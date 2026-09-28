# https://projecteuler.net/problem=32
from itertools import permutations,combinations
import math
from tqdm import tqdm

digits = [i for i in range(1,10)]

def toInt(x: list[int]) -> int:
    y = 0
    for i in reversed(range(len(x))):
        y += x[-i-1] * 10**i
    return y

def toList(x: int) -> list[int]:
    y = []
    for i in reversed(range(int(math.log10(x))+1)):
        y.append((x // 10**i) % 10)
    return y

# while stacking so many loops especially with multiple `combinations`,
# `permutations` may be scary and produce concerns of factorial time, it will be
# much lower since its essentially 1..10->combo->perm e.g. 9!+8!+7!+..+1!

# find a,b,c such that a*b=c and only contains each digit 1..9 once
found = set([])
with tqdm() as pbar:
    for a_size in range(1,10):
        for a_comb in combinations(digits,a_size):
            b_pos = [x for x in digits if x not in set(a_comb)]
            for a_perm in permutations(a_comb):
                for b_size in range(1,10-a_size):
                    for b_comb in combinations(b_pos, b_size):
                        c_pos = [x for x in b_pos if x not in set(b_comb)]
                        for b_perm in permutations(b_comb):
                            av,bv = toInt(a_perm), toInt(b_perm)
                            cv = av*bv
                            c_perm = toList(cv)
                            pbar.update()
                            # If the remaining digits can be used to construct c with none used twice
                            if len(c_perm) == len(c_pos) and set(c_perm) == set(c_pos) and cv not in found: 
                                found.add(cv)
                                pbar.set_description(f"total: {len(found)}, recent: {av}*{bv}={cv}")
print(sum(found))