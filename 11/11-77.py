from math import ceil, log

K = 12312
B = 50
M = 2000
bi = ceil(log(M)/log(2))

n50 = K // B
ex50 = K % B

bytes50 = ceil( bi*B / 8 )
bytesEx = ceil( bi*ex50 / 8 )

total = ceil( (bytes50*n50 + bytesEx) / 1024 )

print( total )