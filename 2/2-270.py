def fn(x, y, z ,w):
    return (x and not y) or (x == z) or w

from itertools import product, permutations
for a, b, c, d, e, f, g in product([0, 1], repeat=7):
    table = [(1, a, b, c), (1, 1, d, e), (f, 1, g, 1)]
    if len(table) != len(set(table)):
        continue
    for p in permutations('xywz'):
        if all( not fn(**dict(zip(p, r))) for r in table ):
            print(*p)
