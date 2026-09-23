# https://projecteuler.net/problem=42
import math
import os

def triangle(x):
    return 0.5 * x * (x + 1.0)

def isTriangle(y):
    a = (-1.0 + math.sqrt(1 + 8.0*y)) / 2.0
    b = (-1.0 - math.sqrt(1 + 8.0*y)) / 2.0
    check = a.is_integer()
    print(f"{check} {a} {b} {triangle(a)} {triangle(b)}")
    return check

count = 0
with open(os.path.join(os.path.dirname(__file__), "0042_words.txt")) as file:
    for line in file:
        for word in line.strip().split(","):
            word = word.strip().strip('"')
            if not word: continue
            value = sum(ord(c)  - ord("A") + 1 for c in word)
            count += int(isTriangle(value))

print(count)