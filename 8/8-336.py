from functools import cache

digits = '123456789ABCDE'
@cache
def F(l, p):
  if p > 10**3: return 0
  if l == 12: return 1
  return sum( F(l+1, p*int(i, 15)) for i in digits )
print( F(0, 1) )


# Автор: Д. Статный

@cache
def f(l, p):
    if l==12: return 0<p<=10**3
    return sum(f(l+1, p*int(i, 15)) for i in '0123456789ABCDE')
print(sum(f(1, int(i, 15)) for i in '123456789ABCDE'))