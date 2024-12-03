
B = 9
def toBase( n ):
  s = ''
  while n:
    s = str(n % B) + s
    n //= B
  return s

def valid( s ):
  if s[0] in ['2','4','6']: return False
  if s[-3] == s[-2] == s[-1]:
    return False
  return True

count = 0
for i in range( int('1000000',B), int('10000000',B) ):
  if valid( toBase(i) ):
     count += 1

print( count )