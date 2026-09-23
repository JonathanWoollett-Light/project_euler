# https://projecteuler.net/problem=4
import math

def isPalindromic(x):
    n = int(math.log10(x))
    # print(f"n: {n}")
    for i in range((n // 2)+1):
        upper = (x // 10**(n-i)) % 10
        lower = (x // 10**i) % 10
        # print(f"upper: {upper}, lower: {lower}")
        if upper != lower: return False
    return True

# print(isPalindromic(1234))
# print(isPalindromic(1221))
# print(isPalindromic(4334))
# print(isPalindromic(232))
# print(isPalindromic(2323))
# print(isPalindromic(956459))

highest = 0
for i in reversed(range(100,999)):
    for j in reversed(range(100,999)):
        x = i * j
        if isPalindromic(x): highest = max(x, highest)
print(highest)
