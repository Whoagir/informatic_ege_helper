from itertools import product

N = 12

count = 0
for w in product('567',repeat=N):
  w = ''.join(w)
  count += '55' not in w

print( count )


def f( L, last = 0 ):
  if L == 0:
    return 1
  return f( L-1, 6 ) + f( L-1, 7 ) + \
         ( f(L-1, 5) if last != 5 else 0)

print( f(N) )

# Автор: Е. Фокин

def s(n):
    a = [0,1]
    b = [0,1]
    c = [0,1]
    for i in range(2,n+1):
        a += [b[i-1] + c[i-1]]
        b += [a[i-1] + b[i-1] + c[i-1]]
        c += [a[i-1] + b[i-1] + c[i-1]]
    return a[n] + b[n] + c[n]
print(s(N))