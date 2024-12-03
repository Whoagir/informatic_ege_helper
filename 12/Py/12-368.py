def alg( s ):
  while '00' not in s:
    s = s.replace('01', '320', 1)
    s = s.replace('02', '1203', 1)
    s = s.replace('03', '210', 1)
  return s

results = []
for k1 in range(30):
  for k2 in range(30):
    for k3 in range(30):
      s = '0' + k1*'1' + k2*'2' + k3*'3' + '0'
      r = alg( s )
      if r.count('1') == 11 and r.count('2') == 15:
        print( k1 + k2 + k3 + 2 )
        results.append( k1 + k2 + k3 + 2 )

print( min(results) )