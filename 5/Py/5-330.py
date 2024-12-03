
Rmax = 0
for N in range(1,200):
  s = f"{N:b}"
  if N % 3 == 0:
    s += s[-3:]
  else:
    s += f"{3*(N%3):b}"
  R = int(s, 2)
  if R <= 170:
    Rmax = max( R, Rmax )

print( Rmax )
