from fnmatch import fnmatch

data = [ int(x) for x in open("17-346.txt") ]

def prodDigits( n ):
  p = 1
  while n:
    p *= n % 10
    n //= 10
  return p

def validTriple( a, b, c ):
  p = prodDigits(a)*prodDigits(b)*prodDigits(c)
  valid = p < 2_000_000_000 and fnmatch( str(p), '43*6*' )
  return valid, p

count, ma = 0, 0
for a, b, c in zip( data, data[1:], data[2:] ):
  valid, p = validTriple( a, b, c )
  if valid:
    count += 1
    ma = max( ma, p )

print( count, ma )

