n = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5  - 5*25**4-  2025

def zeros( n, b ):
  count = 0
  while n:
    count += (n % b == 0)
    n //= b
  return count

print( zeros( n, 25) )