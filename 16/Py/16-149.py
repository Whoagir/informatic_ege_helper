def F( n, m ):
  result = 0
  while m <= n:
    if n % m == 0:
      result += 1
    m += 1
  return result

print( F(107864, 3) )
