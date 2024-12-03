
minS, nMin = 10**10, 0
for n in range(1,1000):
  s = '1'*33+ '2'*33 + '3'*n
  while '11' in s or '22' in s or '13' in s or '23' in s:
    s = s.replace( '11', '2', 1)
    s = s.replace( '22', '1', 1)
    s = s.replace( '13', '2', 1)
    s = s.replace( '23', '1', 1)
  if int(s) < minS:
    minS, nMin = int(s), n


print( minS, nMin )

