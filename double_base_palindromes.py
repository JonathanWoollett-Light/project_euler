# https://projecteuler.net/problem=36
import math

def isPalindromic(x, base):
    n = int(math.log(x, base))
    # print(f"n: {n}")
    for i in range((n // 2)+1):
        upper = (x // base**(n-i)) % base
        lower = (x // base**i) % base
        # print(f"upper: {upper}, lower: {lower}")
        if upper != lower: return False
    return True


# print(isPalindromic(585, 10))
# print(isPalindromic(585, 2))

x = 0
for i in range(1,1_000_000):
    if isPalindromic(i, 10) and isPalindromic(i, 2):
        x += i
print(x)