
minCount = 1e10
start = 101
for i in range(start, start+100):
  s = "1"*i
  while '1111' in s:
    s = s.replace( '1111', '2', 1 )
    s = s.replace( '22', '11', 1 )
  count = s.count('1')
  if count < minCount:
    print( i, "->", count )
    minCount = count

