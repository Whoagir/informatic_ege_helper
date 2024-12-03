s = '7'*100
while '333' in s or '77777' in s:
  if '333' in s:
    s = s.replace('333', '77', 1)
  else:
    s = s.replace('77777', '7', 1)
print( sum( map(int, s) ) )