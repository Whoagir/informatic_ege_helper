from sys import setrecursionlimit


def F(n, m):
    if n < m:
        n, m = m, n
    if n != m:
        return F(n - m, m)
    else:
        return n


setrecursionlimit(3000)
minnm = 1000
for a in range(1, 50):
    for b in range(1, 50):
        if F(a, b) > 15 and a != b and a + b < minnm:
            print(a, b, F(a, b))
            minnm = a + b