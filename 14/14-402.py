import string

A = string.digits + string.ascii_uppercase

for p in range(2, 37):
  for x in A[0:p]:
    sx = f'1{x}77'
    sy = f'{x}{x}77'
    for y in A[1:p]:
      ss = f'{y}0{y}{y}'
      try:
        if int( sx, p ) + int( sy, p) == int( ss, p ):
          print( x, y, p )
          print( int( f'{y}{x}{y}{x}', p ) )
      except:
        pass


