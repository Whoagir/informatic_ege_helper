def valid( s ):
  s = sum( int(x) for x in s[:-1] )
  return s == 68

def f( s ):
  while '>1' in s or '>2' in s or '>0' in s:
    if '>1' in s:
      s = s.replace( '>1', '22>', 1 )
    if '>2' in s:
      s = s.replace( '>2', '2>', 1 )
    if '>0' in s:
      s = s.replace( '>0', '1>', 1 )
  return s

n = 1
while not valid( f('>'+n*'1'+12*'0'+8*'2') ):
  n += 1

print( n )