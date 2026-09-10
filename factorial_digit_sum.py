import math

n = 100

a = 1
for i in range(1,n+1):
    a *= i
print(a)

b = 0
for i in range(1,int(math.log10(a))+1):
    b += (a // 10 ** i) % 10
print(b)