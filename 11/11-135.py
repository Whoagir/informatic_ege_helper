from math import ceil, log2

M = 26 + 10
i = ceil( log2(M) )
#print(i)

Iid = ceil( 22*i/8 )
print(Iid)

Iart = ceil( log2(1_000_000) )
Icount = ceil( log2(1_000) )
Iblock = ceil( (Iart+Icount) / 8 )
print( Iblock )

print( Iid + 30*Iblock )

Itotal = 6*1024*1024 / 32768

print( Itotal )

print( Itotal - (Iid + 30*Iblock) )



