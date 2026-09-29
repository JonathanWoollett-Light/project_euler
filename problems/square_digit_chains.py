# https://projecteuler.net/problem=92
import math
from tqdm import tqdm


# all square chains arriveat 1 or 89, count the number that arrive at 89, starting from numbers below 10 million

# each number ends up computing a chain of numbers that link together
squares = [i**2 for i in range(0,10)]
# a directed graph where every node has 1 child, a functional graph
# the optimization is that if we know a->b->c, then we know a->c and so a should be pointed to c
graph = {}
eighty_nines = 0
n = 10_000_000
with tqdm(total=n-1) as pbar:
    for i in range(1,n):
        prev = i
        seen = []
        while(True):
            if prev not in graph: graph[prev] = sum([squares[(prev // 10**k) % 10] for k in range(int(math.log10(prev))+1)])
            seen.append(prev)
            next = graph[prev]

            # break on first repeat
            if next == 89:
                eighty_nines += 1
                # pbar.set_description(f"eighty_nines: {eighty_nines}, len(graph): {len(graph)}, {len(graph) / i}")
                break
            if next == 1: break
            prev = next

        # point all in seen chain at the last value which will be 89 or 1
        assert graph[prev] == 1 or graph[prev] == 89
        for s in seen: graph[s] = graph[prev]

        pbar.update()
print(eighty_nines)