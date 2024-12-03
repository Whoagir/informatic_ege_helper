x = -1
for n1 in range(23):
 for n2 in range(52):
  for n3 in range(23):
    if n1+n2+n3 == 51 and n1+2*n3 == 29 and n1+n3 == 23:
      print( n1, n2, n3 )
      x, y, z = n1, n2, n3
      break
  if x >= 0: break
 if x >= 0: break

print('--------------------------------------')

# проверка

s = '0' + '1'*x + '2'*y + '3'*z
while '01' in s or '02' in s or '03' in s:
  s = s.replace('01', '2302', 1)
  s = s.replace('02', '10', 1)
  s = s.replace('03', '201', 1)
  print(s)

print( s.count('1'), s.count('2'), s.count('3') )

print('--------------------------------------')

found = False
for n1 in range(23):
 for n2 in range(52):
  for n3 in range(23):
    s = '0' + '1'*n1 + '2'*n2 + '3'*n3
    while '01' in s or '02' in s or '03' in s:
      s = s.replace('01', '2302', 1)
      s = s.replace('02', '10', 1)
      s = s.replace('03', '201', 1)
    if s.count('1') == 51 and s.count('2') == 29 and s.count('3') == 23:
      print( n1, n2, n3 )
      found = True
      break
  if found: break
 if found: break
