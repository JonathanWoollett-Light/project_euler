import math

n = 1000
n += 1
counts = dict([(p,set([])) for p in range(1,n)])
for a in range(1, n):
    for b in range(1, n): # can properly just restrict this based on `a` rather than needing `set`
        c = math.sqrt(a**2 + b**2)
        p = int(a + b + c)
        if c.is_integer() and p < n:
            p = int(a + b + c)
            counts[p].add(min(a,b))
            if p == 120: print(f"a: {a}, b: {b}, c: {c}, math.sqrt(a**2+b**2): {math.sqrt(a**2+b**2)}, c**2: {c**2}")


max_key = None
max_value = 0
for k,v in counts.items():
    if len(v) > max_value:
        max_value = len(v)
        max_key = k
print(max_key)
print(max_value)