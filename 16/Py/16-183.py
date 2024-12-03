# Автор: Е. Джобс

from functools import lru_cache

@lru_cache(None)
def F(n):
    if n >= 3210:
        return 1
    return F(n+3) + 7

@lru_cache(None)
def G(n):
    if n < 10:
        return n
    return G(n-3) + 5

for i in range(3210, 15, -1):
    F(i)

for i in range(10, 3000):
    G(i)

print(F(15) - G(3000))

