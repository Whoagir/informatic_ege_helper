TARGET = 35
count = 0
for x in range(100, 1000):
  s = sorted( str(x) )
  if s[0] == '0':
    if s[1] == '0':
      mi = ma = int(s[2]+'0')
    else:
      mi = int( s[1] + '0' )
      ma = int( s[2] + s[1] )
  else:
    mi = int( s[0] + s[1] )
    ma = int( s[2] + s[1] )
  R = ma - mi
  if R == TARGET:
    print( x )
    count += 1

print( count )


