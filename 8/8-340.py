from functools import cache

@cache
def F(l = 0, lastDigit = -1, countB = 0 ):
  if l == 7: return int(countB == 2)
  k = 0
  for i in range(0 if l > 0 else 1, 30):
    if lastDigit != i:
      if i == int('B',30):
        if countB < 2:
          k += F( l + 1, i, countB+1  )
      else:
        k += F( l + 1, i, countB )
  return k

print( F() )


# Автор Д. Статный

@cache
def f(c, l, k11):
    k11 += c==11
    if l==7: return k11==2
    count = 0
    for j in range(30):
        if j!=c:
            count += f(j, l+1, k11)
    return count
print(sum(f(i, 1, 0) for i in range(1, 30)))
