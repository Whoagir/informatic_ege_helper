def f( s ):
  while '00' not in s:
    s = s.replace( '02', '101', 1 )
    s = s.replace( '11', '2', 1 )
    s = s.replace( '12', '21', 1 )
    s = s.replace( '010', '00', 1 )
  return s

def isSpec( n ):
  return all( int(d) % 2 == 0 for d in str(n) )

for n in range(125, 200):
  s = '0' + n*'1' + n*'2' + '0'
  s1 = f(s)
  sumDig = sum( map(int, s1) )
  if isSpec(sumDig):
    print( n, sumDig )
    break
