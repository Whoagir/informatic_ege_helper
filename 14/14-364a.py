import string

alpha = '0123456789' + string.ascii_uppercase + string.ascii_lowercase
alpha = alpha[:55]

def fromBase( s, base ):
  n = 0
  for c in s:
    d = alpha.index(c)
    n = base*n + d
  return n

results = []
for a in alpha:
  diff = fromBase( f"Z{a}YX", 55 ) - fromBase( f"2X{a}Y", 55 )
  if diff % 29 == 0:
    print( a, diff )
    results.append( (a, diff) )

print( 'Ответ:', results[-1][1] - results[0][1] )



