data = [ x.strip() for x in open("17-362.txt") ]
import string
alpha = '0123456789' + string.ascii_uppercase

def fromBase( s, base ):
  n = 0
  for c in s:
    d = alpha.index(c)
    n = base*n + d
  return n

def base( s ):
  b = max( alpha.index(c) for c in s ) + 1
  return fromBase(s, b), b

count = maxSum = 0
for a, b in zip(data, data[1:]):
  a, ba = base(a)
  b, bb = base(b)
  if abs(ba - bb) <= 2:
    count += 1
    maxSum = max( maxSum, a+b  )

print( count, maxSum )