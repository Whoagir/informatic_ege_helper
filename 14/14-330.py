x = 18**105 + 25*16**100 - 3**51  + 15**90
print( hex(x).count('66') )
s = hex(x)
count = 0
for a, b in zip(s,s[1:]):
  if a == b == '6':
    count += 1
print( count )    
  