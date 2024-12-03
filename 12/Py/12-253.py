
minCount = 1e10
start = 101
for i in range(start, start+100):
  s = "1"*i
  while '111' in s:
    s = s.replace( '111', '2', 1 )
    s = s.replace( '2222', '333', 1 )
    s = s.replace( '33', '1', 1 )
  count = s.count('1')
  #print( i, "->", count )
  if count < minCount:
    print( i, "->", count )
    minCount = count

