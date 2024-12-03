# Автор: К. Багдасарян

def f( n ):
    al = '0123456789AB'
    return al[n] if n < 12 else \
           f(n // 12) + al[n%12]

Rmin = 10**10
for N in range(12, 1000):
    s = f(N)
    if N % 12 == 0:
        s += s[-2:]
    else:
        s += f( (N % 12)*9 )
    R = int(s, 12)
    if R > 300 and R < Rmin:
        Rmin = R
print(Rmin)
