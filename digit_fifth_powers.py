
import math


# ((x/10^n)%10)^5 where `n=log10(x)`
# ((x/10^1)%10)^5 + ((x/10^2)%10)^5 + ((x/10^3)%10)^5 + + ((x/10^6)%10)^5
# (0..9)^5 + (0..9)^5 + (0..9)^5 + (0..9)^5  at most equals (log10(x)+1)*9^5 ~= O(log n)
# Since broadly the a summation of digits to a power scales at O(log n) it likely informs the lower bound
# So at what point is does (log10(x)+1)*9^5=x, solving for x ~= 389_139

record = []
for i in range(2,389_139):
    total = 0
    for j in range(int(math.log10(i))+1):
        total += ((i // 10**j) % 10)**5
    if total == i: record.append(i)
total = sum(record)
print(total)