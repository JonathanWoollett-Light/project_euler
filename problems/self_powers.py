# https://projecteuler.net/problem=48

# 1^1 + 2^2 + 3^3 + 4^4 + .. + 10^10 = 10_405_071_317


digits = 10
kept = 10**digits
n = 1000
x = 0
y = 0
for i in range(1,n+1):
    temp = i
    for j in range(i-1):
        temp *= i
        temp %= kept
        # print(f"\t{temp}")
    # print(temp)
    x += temp
    x %= kept
    y += i**i
print(y)
print(x)