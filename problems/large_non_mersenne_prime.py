# https://projecteuler.net/problem=97
# there is a prime with 2_357_207 digits which equals 28433 * 2**7830457 + 1
# find the last ten digits of this prime

rem = 10**10
x = 1
y = 1
for i in range(7830457):
    x *= 2
    x %= rem
    if i < 30:
        y *= 2
        print(f"{y % rem}, {x}")
        assert y % rem == x
x *= 28433
x += 1
print(x % rem)