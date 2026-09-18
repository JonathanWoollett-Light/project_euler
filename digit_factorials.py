# multiplication -> prime?

# 1! + 2! + 3! + 4! = 1 + 1*2 + 1*2*3 + 1*2*3*4
# cheaper way to calculate:
# 1! + 2! + 3! + 4! = 1 + 2 * (1 + 3 * (1 + 1*4)

# 1! -> 2! -> 3! -> 4! -> .. -> 1!+0! -> 1!+1! -> 1!+2! -> 1!+3! -> 1!+4! -> ..
# 1  -> 2  -> 6  -> 24 -> .. -> 2     -> 2     -> 3     -> 7     -> 25    -> ..
# so we can store the factorials up to 9, then just add these together later

# possibly you can also exclude certain factorials from the search, this may be
# where primes come in

# if there is a sum, then there's a finite number, so whats the upper limit?
# 1! + 1! + .. + 1! < 11..1
# 1! + 1! + .. + 2! < 11..2
# 

# [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
# the space between numbers which are the sum of their factorial digits will always increase?

# `a!b!=b!+a!``, if a+b = "ab", skip `b!+a!`
# 0,1,2,3,4,5,6,7,8,9, all of (0,1),(0,2),(0,3),(0,4),(0,5),... are already covered
# thus the lowest digit is 0..9, then the next is 1..9, then the next is 2..9?
# produces unique combinaions of digits, so you could iterate over each unique factorial combination

import math

factorials = [1]
for i in range(1,10):
    factorials.append(factorials[-1] * i)
print(factorials)

count = 1
upper_limit = factorials[9]
while (count < upper_limit):
    indexs = [(count // 10**i) % 10 for i in reversed(range(int(math.log10(count))+1))]
    set = [factorials[i] for i in indexs]
    # print(set)
    a = sum(set)
    b = "".join([str(x) for x in indexs])
    if str(a) == b: print(a)
    # print(f"{indexs} -> {set} -> {b} {a}")
    count += 1


# so with some help, where is 10**(n-1) > n*9!, this is the upper limit, since
# 10*8(n-1) will afterwards continue to outgrow n*9!
# when looking for limits and finite sets, its important to categorize which
# factors grow linearly, polynomially, exponentially, etc.