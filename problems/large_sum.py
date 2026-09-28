# https://projecteuler.net/problem=13
import os
import math

numbers = []
with open(os.path.join(os.path.dirname(__file__), "0013_digits.txt"), "r") as file:
    numbers = [int(line) for line in file if line.strip()]

print(f"read {len(numbers)} numbers")

# python big ints make this trivial
total = 0
for num in numbers: total += num
first = total // (10**(int(math.log10(total)) - 9))
print(total)
print(first)