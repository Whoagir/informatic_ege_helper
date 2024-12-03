
def alg( s ):
  while '37' in s or '577' in s or '777' in s:
    if '37' in s:
      s = s.replace( '37', '7', 1 )
    if '577' in s:
      s = s.replace( '577', '73', 1 )
    if '777' in s:
      s = s.replace( '777', '5', 1 )
  return s

def coprime( a, b ):
  return all( not(a % d == 0 and b % d == 0) for d in range(2,min(a,b)+1) )

for n in range(10, 100):
  s = '3' + n*'7'
  s1 = alg( s )
  sd = sum( map(int, s1) )
  if 10 <= sd <= 99 and coprime( n, sd ):
    print( n )

