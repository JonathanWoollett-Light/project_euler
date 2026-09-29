# https://projecteuler.net/problem=74
import math
from tqdm import tqdm
# count the number of numbers for which you can perform  the sum of the
# factorials of their digits recursively for exactly 60 iterations without
# encountering a duplicate.

# here we could probably optimize paths by using some type of tree/graph so when we encounter a
# given `fsum` we know in how many steps it will lead to `i` if it does, then we can immedately
# skip along a number of steps, 60*1_000_000*math.log10(..) is tractable but still longer than 1
# minute recommended for project euler stuff

# each number ends up computing a chain of numbers that link together
facts = [math.factorial(i) for i in range(0,10)]
# a directed graph where every node has 1 child, a functional graph

# i still think this can be optimized further but this solution resolves in 8 seconds so thats good
# enough
graph = {}
sixty_chains = 0
n = 1_000_000
with tqdm(total=n-1) as pbar:
    for i in range(1,n):
        prev, seen  = i, set([i])
        while(True):
            if prev not in graph: graph[prev] = sum([facts[(prev // 10**k) % 10] for k in range(int(math.log10(prev))+1)])
            next = graph[prev]
            # break on first instance of `i` so it can't do a cycle through many instances of `i`
            # until it hits 60 steps
            if next in seen: break
            seen.add(next)
            prev = next
            
        if len(seen) == 60:
            sixty_chains += 1
            pbar.set_description(f"sixty_chains: {sixty_chains}")
        pbar.update()
    