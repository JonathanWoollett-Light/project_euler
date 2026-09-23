# https://projecteuler.net/problem=2
a = 1
b = 2
evens = 0
while(b < 4_000_000):
    if b % 2 == 0: evens += b
    c = b
    b += a
    a = c
print(evens)