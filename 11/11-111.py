from math import *

M = 10 + 1650
i = log(M)/log(2)
print( f"i = {i}" )
i = ceil( i )
print( f"i = {i} bits" )
i = ceil( i / 8 )
print( f"i = {i} bytes" )

I = 253*i
print( f"I = {I}" )
while I % 10 != 0:
  I += 1
print( f"I = {I}" )

II = 65536 * I // 1024
print( f"II = {II}" )