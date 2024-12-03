x = 49**129 + 7**131 - 2
h = ""

while x:
  h = str(x % 7) + h
  x //= 7

for d in '6543210':
  if h.count(d) > 0: break

h = h.replace( '0', d )

print( d, h.count(d) )
