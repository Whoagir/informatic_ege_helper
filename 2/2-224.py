from itertools import product
def f(x, y, z, w):
  return (not (x <= z)) or (y == w) or y

for x, y, z, w in product([0, 1], repeat = 4):
  if f(x, y, z, w) == 0:
     print( f"{x}{z}{w}{y}" )
