# Автор: К. Багдасарян

def f( n ):
    return str(n) if n < 5 else \
           f(n // 5) + str(n%5)

Rmin = 10**10
for N in range(5, 1000):
    s = f(N)
    if N % 5 == 0:
        s += s[-2:]
    else:
        s += f( (N % 5)*7 )
    R = int(s, 5)
    if R > 200 and R < Rmin:
        Rmin = R
print(Rmin)


