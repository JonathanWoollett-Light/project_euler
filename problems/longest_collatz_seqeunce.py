# https://projecteuler.net/problem=14
from tqdm import tqdm

step = lambda x: x // 2 if x % 2 == 0 else 3*x+1
max_steps = []
n = 1_000_000
with tqdm(total=n) as pbar:
    for i in range(n):
        steps = [i]
        while (steps[-1] > 1): steps.append(step(steps[-1]))
        if i == 13: print(f"{i}: {steps}")

        if len(steps) > len(max_steps):
            max_steps = steps
            pbar.set_description(f"{len(max_steps)}: {max_steps[:5]}..{max_steps[-10:]}")
        pbar.update()
print(len(max_steps))