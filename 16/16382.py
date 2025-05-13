from sys import setrecursionlimit


def f(n):
    if n<=3:
        return 2025
    if n>3:
        return 3*(n-1)*f(n-2)
setrecursionlimit(3000)
print(f(2027)//f(2023))