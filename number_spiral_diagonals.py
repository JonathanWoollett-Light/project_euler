# https://projecteuler.net/problem=28
# 1^2 + 3^2 + 5^2 + ..
# n = 5
n = 1001
total = 1
for i in range(3,n+1,2):
    b = i**2
    c = i-1
    total += b + (b-1*c) + (b-2*c) + (b-3*c)
    # print(total)

print(total)