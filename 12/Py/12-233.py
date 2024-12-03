
s = '1121121121121121111111111111'
print(s.count('1'), s.count('2'))

while '11' in s:
  if '112' in s:
    s = s.replace( '112', '5', 1 )
  else:
    s = s.replace( '11', '3' )
  print( s )

print( s )
print( sum( map(int,s) )  )
