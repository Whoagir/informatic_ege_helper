def f(a, n):
    return sum(a[::-1][i]*n**i for i in range(len(a)))

p = 7
found = False
while not found:
  for x in range(p):
   for y in range(p):
      if f([3,4],p)*f([5,6],p) == f([x,y,2],p):
         print( p, x, y, f([y,x],p) )
         found = True
         break
  p += 1
