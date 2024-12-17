def F(n):
    if n<7:
        return 7
    else:
        return n+1+F(n-2)
import sys
sys.setrecursionlimit(2000)
print(F(2024)-F(2020))