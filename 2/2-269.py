def fn(x, y, z ,w):
    return (x or not y) and (x != z) and not w

from itertools import product, permutations
for a, b, c, d in product([0, 1], repeat=4):
    table = [(0, 0, 1, a), (0, b, 0, 1), (c, 1, 1, d)]
    if len(table) != len(set(table)):
        continue
    for p in permutations('xywz'):
        if all( fn(**dict(zip(p, r))) for r in table ):
            print(*p)
