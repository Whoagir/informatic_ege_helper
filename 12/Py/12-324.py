def f( s ):
  count = 0
  while '3333' in s or '222' in s:
    if '3333' in s:
      s = s.replace( '3333', '2', 1 )
    else:
      s = s.replace( '222', '3', 1 )
    count += 1
  return s, count

n = 1
while f(n*'3') != ('22', 34):
  n += 1

print( n )