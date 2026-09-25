# https://projecteuler.net/problem=59
from itertools import product,cycle
import enchant
import os
import string

# read file
numbers = []
with open(os.path.join(os.path.dirname(__file__), "0059_cipher.txt"),"r") as f:
    numbers = [int(x) for x in f.read().split(",")]

d = enchant.Dict("en_US")
r = range(ord('a'),ord('z'))

print(f"len(numbers): {len(numbers)}")

def check(key):
    text = ''.join(chr(v ^ k) for v, k in zip(numbers, cycle(key)))
    if not all(c in string.printable for c in text): return -1
    words = (w.strip(string.punctuation) for w in text.split())
    return sum(1 for w in words if w and d.check(w))

best = max(product(r, r, r), key=check)
print(best)
sum = sum([v ^ k for k,v in zip(numbers, cycle(best))])
print(sum)