
x = 0
N = 0
while N < 10**6:
   x += 1
   N = 2*(x-1)*(3*x-1) + 2*(x-1)*(x+1)

print( x - 1 )