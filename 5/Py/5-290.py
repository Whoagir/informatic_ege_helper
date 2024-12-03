def alg( n ):
  n = sum( map(int, str(n)) )
  s = f"{n:b}"
  if s.count('1') % 2 == 0:
    s = '1' + s + '00'
  else:
    s = '10' + s + '1'
  return int( s, 2 )

count = 0
allVarsWithSum2 = [
'110000000',  '101000000',
'100100000',  '100010000',
'100001000',  '100000100',
'100000010',  '100000001',
'200000000', ]
for var in allVarsWithSum2:
  if alg( int(var) ) == 21:
    count += 1

print( count )