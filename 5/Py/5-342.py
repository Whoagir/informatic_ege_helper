# Автор: К. Багдасарян

def f( n ):
    al = '0123456789ABCDE'
    return al[n] if n < 15 else \
           f(n // 15) + al[n%15]

Rmin = 10**10
for N in range(15, 1000):
    s = f(N)
    if N % 15 == 0:
        s += s[:2]
    else:
        s += f( (N % 15)*13 )
    R = int(s, 15)
    if R > 700 and R < Rmin:
        Rmin = R
print(Rmin)
