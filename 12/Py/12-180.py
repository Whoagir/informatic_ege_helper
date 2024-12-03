s = 500*"5"

count = 0
while '333' in s or '555' in s:
  if '333' in s:
    s = s.replace( '333', '5', 1 )
    count += 3
  else:
    s = s.replace( '555', '3', 1 )

print( count )
