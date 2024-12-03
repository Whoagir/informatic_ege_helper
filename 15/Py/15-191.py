P = set( range(10, 18+1) )
Q = set( range(8, 30+1) )
U = set( range(1000) )
A = set()
for x in U:
  if ((not x in A) <=((x in P) <= (x in (U-Q)))) == False:
    A.add(x)
print( A )
print( len( [x for x in A if x % 2 == 1] ) )