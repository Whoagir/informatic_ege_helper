from functools import cache

@cache
def F(l = 0, counters = '000000000'):
  if l == 10: return 1
  k = 0
  for i in range(0 if l > 0 else 1, 9):
    if counters[i] < '2':
      c2 = counters[:i] + chr(ord(counters[i])+1) + counters[i+1:]
      k += F( l+1, c2 )
  return k

print( F() )

@cache
def F(l = 0, counters = (0,)*9):
  if l == 10: return 1
  k = 0
  for i in range(0 if l > 0 else 1, 9):
    if counters[i] < 2:
      c2 = counters[:i] + (counters[i]+1,) + counters[i+1:]
      k += F( l+1, c2 )
  return k

print( F() )


# Автор Д. Статный

from time import time
#№1
#ОПТИМИЗИРОВАННОЕ РЕШЕНИЕ ДЛЯ БОЛЬШОЙ ДЛИНЫ, ДАБЫ НЕ ХРАНИТЬ БОЛЬШУЮ СТРОКУ
#ПРОВЕРКА НА ПОВТОР ЧИСЛА ОСУЩЕСТВЛЯЕТСЯ ЧЕРЕЗ ВЫЧИСЛЕНИЕ
#СТЕПЕНИ ВХОЖДЕНИЯ 10-КИ В НАКАПЛИВАЕМУЮ СУММУ
st = time()
@cache
def f(d, l):
    if l == 10: return 1
    return sum(f(d+10**(int(i)+1), l+1) for i in '012345678' if (d//10**(int(i)+1))%10<2)
print(sum(f(10**(int(i)+1), 1) for i in '12345678'))
print(time()-st)
#НЕОПТИМИЗИРОВАННАЯ РЕКУРСИЯ ПОД МАЛЕНЬКУЮ ДЛИНУ (АДЕКВАТНО РАБОТАЕТ ДЛЯ ДЛИНЫ <8)
#@cache
#def f(s, l):
#    if l==7: return 1
#    return sum(f(s+i, l+1) for i in '012345678' if s.count(i)<2)
#print(sum(f(i, 1) for i in '12345678'))
#print(time()-st)
