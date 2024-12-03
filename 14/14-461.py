# Автор: PRO100-ЕГЭ

for x in range(10000):
  n = 4*625**1920 + 4*125**x - 4*25**1940 - 3*5**1950 - 1960
  count = 0
  while n:
    count += ((n % 5) == 0)
    n //= 5
  if count == 1891:
    print( x )
    break

