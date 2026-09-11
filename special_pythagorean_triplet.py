from math import isqrt

N = 500_000          # (1000 - a)(1000 - b) = 500000 = 2**5 * 5**6

# every divisor, straight from the prime factorisation
divisors = sorted(2**i * 5**j for i in range(6) for j in range(7))

for x in divisors:
    # x < 1000 keeps a positive; x > sqrt(N) forces y < x, i.e. a < b
    if isqrt(N) < x < 1000:
        y = N // x
        a, b = 1000 - x, 1000 - y
        c = 1000 - a - b
        print(f"a={a}, b={b}, c={c}, product={a*b*c}")