def F(n):
    if (int(n ** (1 / 2)) ** 2 == n):
        return n ** (1 / 2)
    else:
        return F(n + 1) + 1


import sys

sys.setrecursionlimit(10000)
print(F(4850) + F(5000))
