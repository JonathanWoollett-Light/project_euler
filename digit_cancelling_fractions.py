# a fraction is curious if by cancelling common digits in the numerator and
# # denominator the result is a fraction which has the same value as the
# original fraction e.g. 49/98 = 4/8 (cancelling the common 9s)

import math

def isCurious(a,b) -> bool:
    if a == b: return (False,a,b)

    # Extract unique digits preserving positions
    a_digits = {}
    for i in range(int(math.log10(a))+1):
        x = (a // 10**i) % 10
        a_digits[x] = i
    b_digits = {}
    for i in range(int(math.log10(b))+1):
        x = (b // 10**i) % 10
        b_digits[x] = i
    
    # if a == 49 and b == 98: print(f"a_digits: {a_digits}, b_digits: {b_digits}")

    # Remove duplicate digits
    unique_a_digits = [(k,v) for k,v in a_digits.items() if not (k in b_digits)]
    unique_b_digits = [(k,v) for k,v in b_digits.items() if not (k in a_digits)]

    # If there are only unique digits
    if len(unique_a_digits) == len(a_digits) and len(unique_b_digits) == len(b_digits): return (False, a, b)

    # An ordering preserving map would be more efficient, to avoid this sorting.

    # Sort based on positions
    keyFunc = lambda x: x[1]
    unique_a_digits.sort(key=keyFunc)
    unique_b_digits.sort(key=keyFunc)
    # if a == 74 and b == 98: print(f"unique_a_digits: {unique_a_digits}, unique_b_digits: {unique_b_digits}")
    # if a == 49 and b == 98: print(f"unique_a_digits: {unique_a_digits}, unique_b_digits: {unique_b_digits}")

    # Re-construct a and b
    new_a = 0
    for i,(k,v) in enumerate(unique_a_digits):
        new_a += k * 10**i
    new_b = 0
    for i,(k,v) in enumerate(unique_b_digits):
        new_b += k * 10**i

    # if a == 74 and b == 98: print(f"{new_a} / {new_b} ({new_a/new_b}) == {a} / {b} ({a/b})")
    # if a == 49 and b == 98: print(f"{new_a} / {new_b} ({new_a/new_b}) == {a} / {b} ({a/b})")
    if new_a == 0 or new_b == 0: return (False, new_a, new_b)
    return (new_a / new_b == a / b,new_a,new_b)

# start at 11 since both a and b must have 2 digits
product_a = 1
product_b = 1
product = 1
for b in range(11,100):
    for a in range(11,b): # if a/b<1, then b>a
        if a % 10 == 0 and b % 10 == 0: continue
        is_curious, new_a,new_b = isCurious(a,b)
        if is_curious:
            print(f"{a}/{b} == {new_a}/{new_b}")
            product_a *= new_a
            product_b *= new_b
            product *= new_a/new_b
print(f"{product:.5}")

gcd = math.gcd(product_a,product_b)
print(gcd)
lowest_a = product_a / gcd
lowest_b = product_b / gcd
print(f"{lowest_a} / {lowest_b} == {lowest_a/lowest_b:.5} == {product_a} / {product_b} == {product_a / product_b:.5} == {product:.5}")