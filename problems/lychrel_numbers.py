# https://projecteuler.net/problem=55

# a reverse-add operation is done by flipping the digits of a given number and
# adding it to the original number e.g. 47 -> 47 + 74
#
# a number is lychel when it never becomes a palindrome after any number of
# reverse-add operations

# Count the number of lychel number below 10,000
# if it doesn't become a palindrome in 50 steps, assume it never does

import math

def reverseAdd(x: int) -> int:
    n = int(math.log10(x))
    y = x
    for i in range(n+1):
        a = (x // 10**i) % 10
        b = a * 10**(n-i)
        y += b
        # print(f"{a}, {b}, {x}->{y}")
    return y
        

assert reverseAdd(47) == 121

# there may also be a way to check if a reverse will result in a palindrome rather than just
# checking the result, but this is a constant time cost change
def isPalindrome(x: int) -> bool:
    n = int(math.log10(x))
    for i in range((n+1) // 2):
        a = (x // 10**i) % 10
        b = (x // 10**(n-i)) % 10
        if a != b: return False
    return True

assert isPalindrome(121)
assert isPalindrome(212)
assert isPalindrome(33)
assert isPalindrome(3)
assert isPalindrome(321123)
assert isPalindrome(3213123)

# these follow a tree, so we could do some faster jumping to skip steps, but the
# problem is already tractable so we don't need that.
count = {}
lim = 10_000
for i in range(1,lim):
    x = i
    if i == 47 or i == 349 or i == 4994: print(f"{x}", end="")
    for _ in range(50):
        x = reverseAdd(x)
        if i == 47 or i == 349 or i == 4994: print(f"->{x}", end="")
        if isPalindrome(x):
            count[i] = x
            if i == 47 or i == 349 or i == 4994: print()
            break
    if i == 47 or i == 349 or i == 4994: print()
# print(count)
print()
print(list(count.items())[:20])
print(count[47])
print(count[349])
# print(count[4994])
print(196 in count)
print(lim-len(count)-1)
