
maxCount = -1
start = 71
for i in range(start, start + 100):
  s = "1"*i
  while '111' in s:
    s = s.replace( '111', '22', 1 )
    s = s.replace( '222', '11', 1 )
  count = s.count('1')
  if count > maxCount:
    print( i, "->", count )
    maxCount = count

