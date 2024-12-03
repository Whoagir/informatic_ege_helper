
B = 9
def toBase( n ):
  s = ''
  while n:
    s = str(n % B) + s
    n //= B
  return s

def valid( s ):
  if s[0] in ['3','7']: return False
  for i in range(9):
    if (str(i)+str(i)) in s:
       return False
  return True

count = 0
for i in range( int('1000000',B), int('10000000',B) ):
  if valid( toBase(i) ):
     count += 1

print( count )