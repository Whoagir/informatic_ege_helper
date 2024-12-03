

def f(x,y,A):
   return (680*y + 256*x < A) or (5*x + 3*y > 11112)

A0 = 680*11112//3

for A in range(A0, A0+1000):
    OK = 1
    for x in range(6000):
      for y in range(6000):
         if not f(x,y,A):
            OK = 0
            break
      if not OK: break
    if OK:
        print(A)
        break
