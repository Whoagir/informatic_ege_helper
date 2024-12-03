
maxCount = -1
start = 138
for i in range(start, start+100):
  s = "1"*i
  while '111' in s:
    s = s.replace( '111', '2', 1 )
    s = s.replace( '2222', '1', 1 )
  count = s.count('1')
  if count > maxCount:
    print( i, "->", count )
    maxCount = count

