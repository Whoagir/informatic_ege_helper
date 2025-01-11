from sys import setrecursionlimit


def F(n):
    if n<=2:
        return n
    if n>2:
        return n + F(n-2)
setrecursionlimit(2100)
print(F(2023)+ F(2020))