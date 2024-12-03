def f(a, n):
    return sum(a[::-1][i]*n**i for i in range(len(a)))

p = 6
found = False
while not found:
  for x in range(p):
   for y in range(p):
      if f([2,3],p)*f([4,5],p) == f([x,y,3],p):
         print( p, x, y, f([y,x],p) )
         found = True
         break
  p += 1
