import string

A = string.digits + string.ascii_uppercase

for p in range(2, 37):
  for x in A[1:p]:
    sx = f'397{x}'
    sy = f'{x}9{x}4'
    for y in A[1:p]:
      ss = f'{y}19{y}'
      try:
        if int( sx, p ) + int( sy, p) == int( ss, p ):
          print( x, y, p )
          print( int( f'{x}{x}{y}{y}', p ) )
          found = True
      except:
        pass



