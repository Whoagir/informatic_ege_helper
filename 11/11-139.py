from math import ceil, log2

iChar = ceil( log2(52) )
bFirst = ceil( 8*iChar / 8 )

iDigit = ceil( log2(10) )
iSpec = ceil( log2(3) )
bSecond = ceil( (7*iDigit + iSpec) / 8 )

bPerson = int( 7695 / 285 )

print( bPerson - bFirst - bSecond )