import string

A = string.digits + string.ascii_uppercase

for p in range(2, 37):
  for x in A[1:p]:
    sx = f'5{x}16'
    sy = f'{x}{x}{x}5'
    for y in A[1:p]:
      ss = f'115{y}{y}'
      try:
        if int( sx, p ) + int( sy, p) == int( ss, p ):
          print( x, y, p )
          print( int( f'{y}{x}{y}', p ) )
      except:
        pass



