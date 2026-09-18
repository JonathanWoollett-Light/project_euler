from tqdm import tqdm
import math

def isPermuted(x: int, n: int):
    digits = { 0: 0, 1:0, 2:0, 3:0, 4:0,5:0,6:0,7:0,8:0,9:0 }
    for i in range(int(math.log10(x)) + 1):
        digits[(x // 10**i) % 10] += 1
    # print(f"x: {x} digits: {digits}")
    
    for i in range(1,n+1):
        y = x * i
        temp_digits = { 0: 0, 1:0, 2:0, 3:0, 4:0,5:0,6:0,7:0,8:0,9:0 }
        for j in range(int(math.log10(y)) + 1):
            temp = (y // 10**j) % 10
            # print(f"{temp},",end="")
            temp_digits[(y // 10**j) % 10] += 1
        # print()
        # print(f"y: {y} temp_digits: {temp_digits}")
        if digits != temp_digits: return False
    return True

n = 6
i = 2
with tqdm() as spinner:
    while (True):
        if isPermuted(i, n): break
        i += 1
        spinner.update(i)
for j in range(n+1):
    print(i*j)