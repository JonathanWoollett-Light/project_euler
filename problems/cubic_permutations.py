# https://projecteuler.net/problem=62

# find the smallest cube with exactly 5 permutations which are cubes
# a cube with three permutations is 41063625=345^3 where the digits can
# be re-arranged to equal 384^3 and 405^3

# permutations is factorial scaling versus cube scaling which is linear, so its best to check cube numbers n^3
# so whats the fast way to check if 2 numbers have equal digits? one way is to count the count of digits and
# the number of total digits
# xor'ing every digit should result in 0 if they match and non-zero if they don't, but this doesn't provide a
# key that can be used in a map to track count
# so it might be easiest to go through all the digit inserting them into a min heap, then use this heap as the
# key into a map to count perms of cubes

from tqdm import tqdm

# counting sort
def digit_key(n: int):
    counts = [0] * 10
    while n:
        n, d = divmod(n, 10)
        counts[d] += 1
    return tuple(counts)

counts = {}
final = None
i = 1
with tqdm() as pbar:
    while(True):
        # make each digit set into a key that maps across all permutations
        cube = i**3
        key = digit_key(cube) # O(n+k) -> O(n + 10) -> O(n)

        # add counts
        if key in counts: counts[key].append(cube)
        else: counts[key] = [cube]

        if i == 345 or i == 384 or i == 405:
            pbar.set_description(f"i: {i}, key: {key}, counts[key]: {counts[key]}")

        if len(counts[key]) == 5:
            final = key
            break
        pbar.update()
        i += 1
print(f"{counts[final]}")
print(f"{min(counts[final])}")
