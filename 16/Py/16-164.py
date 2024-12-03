# Автор: Д. Статный

import sys

sys.setrecursionlimit(10_000)
def f(n):
    if n<=400: return 1
    if n>400: return f(n-1)*(n-400)
print(f(701)//f(697))
