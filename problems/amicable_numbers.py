# https://projecteuler.net/problem=21

# d(n) is the sum of all x's for which `n % x == 0`
# `a` and `b` are amicable number if `d(a)=b` and `d(b)=a` and `a!=b`


def sum_divisor(i: int) -> int:
    if i == 220: print(f"set: {[j for j in range(1,i//2 + 1) if i % j == 0]}")
    return sum([j for j in range(1,i // 2 + 1) if i % j == 0])

pairs = set([])
for a in range(10_000):
    if a in pairs: continue

    
    b = sum_divisor(a)
    ab = sum_divisor(b)

    if a == 220: print(f"a: {a}, b: {b}, ab: {ab}")

    if a != b and ab == a:
        pairs.add(a)
        pairs.add(b)


print(len(pairs))
print(sum(pairs))