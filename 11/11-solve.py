from math import log, ceil

N1, A1 = 10, 26
N2, A2 = 8, 10

b1 = ceil(log(A1)/log(2))
b2 = ceil(log(A2)/log(2))

L = N1*b1 + N2*b2
Lbytes = ceil( L / 8 )

print( Lbytes )



