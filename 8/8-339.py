from functools import cache

@cache
def F(l = 0, sEven = 0, sOdd = 0 ):
  if l == 10:
    return int(sEven == sOdd)
  k = 0
  for i in range(0 if l > 0 else 1, 13):
    if i % 2 == 0:
      k += F( l + 1, sEven + i, sOdd )
    else:
      k += F( l + 1, sEven, sOdd + i )
  return k

print( F() )


# Автор Д. Статный

@cache
def f(s1, s2, l):
    if l==10: return s1==s2
    count = 0
    for i in range(13):
        if i%2==0:
            count += f(s1, s2+i, l+1)
        else:
            count += f(s1+i, s2, l+1)
    return count
print( sum(f(i, 0, 1) for i in range(1, 13, 2)) +
       sum(f(0, i, 1) for i in range(2, 13, 2)))
