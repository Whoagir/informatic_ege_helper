def f( n ):
  s = f"{n:b}"
  for _ in range(2):
    if  s.count('1') % 2 == 0:
      s = '11' + s[2:] + '00'
    else:
      s = '10' + s[2:] + '11'
  return int(s,2)

"""
for i in range(100):
  print( i, f(i) )
"""

print( max( f(n) for n in range(100) if f(n) < 1500 ) )
