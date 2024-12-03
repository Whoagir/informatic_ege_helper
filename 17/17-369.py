data = [int(s) for s in open('17-369.txt')]

def isAsc( x ):
  s = str(x)
  return all( int(a) < int(b) for a, b in zip(s, s[1:]) )
def isDesc( x ):
  s = str(x)
  return all( int(a) > int(b) for a, b in zip(s, s[1:]) )

minDesc = min( x for x in data if isDesc(x) )
sMinDesc = sum( map(int, str(minDesc)) )

result = []
for a, b in zip(data, data[1:]):
  if (isAsc(a) ^ isAsc(b)) and a*b % sMinDesc == 0:
     result.append( a + b )

print( len(result), min(result) )
