from functools import lru_cache

@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n + f(n - 1)

for n in range(1, 2024):
    f(n)

c = 0
for n in range(1, 101):
    # print(f(2023) // f(n))
    if f(2023) // f(n) % 2 == 0:
        c += 1
print(c)
