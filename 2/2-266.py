# Автор: Е. Джобс

from itertools import *

def f(x, y, z, w):
    return ((x <= y) or (z == x)) and (w <= z)

t = [(0,0,1,1), (0,0,1,0), (0,1,1,1)]
for p in permutations('xyzw'):
    if [f(**dict(zip(p, r))) for r in t] == [1, 0 ,0]:
        print(*p, sep='')
