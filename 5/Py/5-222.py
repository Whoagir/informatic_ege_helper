
TARGET = 30

count = 0
for x in range(800, 900):
  s = "".join( sorted(str(x), reverse=True) )
  ma = int(s[:2])
  if s[1] == '0' and s[2] == '0':
    mi = ma
  elif s[2] == '0':
    mi = int( s[1] + s[2] )
  else:
    mi = int( s[2] + s[1] )
  # print(x, mi, ma)
  if ma-mi == TARGET:
    print(x, ma, mi)
    count += 1

print( count )


