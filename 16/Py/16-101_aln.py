#16.101_Aвтор А.Л.Наймушин

from functools import lru_cache
@lru_cache
def F( n ):
  if n == 0: return 1
  elif n == 1: return 3
  else:
      if n > 1:
        return F(n-1)- F(n-2) + 3*n


print( F(40 ))

'''
Rez = 126 время около 5 минут
'''
