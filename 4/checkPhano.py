
def phano( codes ):
  for i, c1 in enumerate(codes):
    for j, c2 in enumerate(codes):
      if i != j:
        if c1.startswith(c2) or c2.startswith(c1):
          return False
  return True

def revPhano( codes ):
  for i, c1 in enumerate(codes):
    for j, c2 in enumerate(codes):
      if i != j:
        if c1.endswith(c2) or c2.endswith(c1):
          return False
  return True


busy = ['111', '0100', '1100', '0010', '0001', '0011', '0110', '1001', '1010']
print( 'P:', phano(busy) )
print( 'R:', revPhano(busy) )
busy += ['000']
print( 'P:', phano(busy) )
print( 'R:', revPhano(busy) )