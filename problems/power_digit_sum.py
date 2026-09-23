# https://projecteuler.net/problem=16
import math

n = 1000
a = 2 ** n
print(a)

b = 0
for i in range(0,int(math.log10(a))+1):
    j = (a // 10 ** i) % 10
    # print(j)
    b += j  
print(b)