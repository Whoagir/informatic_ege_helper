from math import ceil, log2

iDay = ceil( log2(31) )
iMonth = ceil( log2(12) )
iYear = ceil( log2(51) )

bDate = ceil( (iDay + iMonth + iYear) / 8 )

iChar = ceil( log2(52) )
bCountry = ceil( 27*iChar / 8 )

bPerson = int( 27*1024 / 1152 )

bNumber = bPerson - bDate - bCountry

iDigit = ceil( log2(10) )
nDigits = int( bNumber*8 / iDigit )

print( 10**nDigits - 1 )
