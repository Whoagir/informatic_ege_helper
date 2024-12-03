s = '0' + '1'*7 + '2'*11 + '3'*21
while '01' in s or '02' in s or '03' in s:
  s = s.replace('01', '302', 1)
  s = s.replace('02', '3103', 1)
  s = s.replace('03', '20', 1)
  print(s)

print( s.count('1'), s.count('2'), s.count('3') )

