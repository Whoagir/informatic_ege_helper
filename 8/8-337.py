from functools import cache

digits = '0123456789'
@cache
def F(l = 0, s = 0):
  if s > 25: return 0
  if l == 12: return 1
  return sum( F(l+1, s+int(i))
              for i in (digits[1:] if l == 0 else digits) )
print( F() )


# Автор: Д. Статный

@cache
def f(s, l):
    if l==12: return s<=25
    return sum(f(s+int(i), l+1) for i in '0123456789')
print(sum(f(int(i), 1) for i in '123456789'))
