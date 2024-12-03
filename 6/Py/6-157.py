
x = 0
N = 0
while N <= 440000:
   x += 1
   N = 2*(x-1)*(4*x-1) + 2*(x-1)*(x+1)

print( x  )