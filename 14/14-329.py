x = 9**81 + 27**729 - 4

s = ""
while x:
  s = str(x % 9) + s
  x //= 9

for d in '876543210':
  if s.count(d) > 0: break

s = s.replace( '0', d )

print( d, s.count(d) )
