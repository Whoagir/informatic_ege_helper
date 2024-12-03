from itertools import product

Alpha = sorted('УЖЕМАЙ')

def valid( s ):
  return all( c+c not in s for c in Alpha )

count = 0
for i, w in enumerate(product( Alpha, repeat = 5)):
   if (i+1) % 2 == 0 and valid( "".join(w) ):
      count += 1

print( count )