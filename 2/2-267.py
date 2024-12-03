# Автор: Е. Джобс

def f1(x, y, z ,w):
    return (x <= y) or ((not w) == z)

def f2(x, y, z, w):
    return (x <= y) == (w and not z)

from itertools import product, permutations
for a, b, c, d, e, f in product([0, 1], repeat=6):
    table = [(a, b, c, 0), (d, e, 0, 0), (f, 0, 0, 0)]
    if len(table) != len(set(table)):
        continue
    for p in permutations('xywz'):
        if [f1(**dict(zip(p, r))) for r in table] \
           == [f2(**dict(zip(p, r))) for r in table]:
            print(*p)
