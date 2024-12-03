import string

A = string.digits + string.ascii_uppercase

for p in range(2, 37):
  for x in A[1:p]:
    sx = f'49{x}9'
    sy = f'{x}6{x}0'
    for y in A[1:p]:
      ss = f'{y}0{y}9'
      try:
        if int( sx, p ) + int( sy, p) == int( ss, p ):
          print( x, y, p )
          print( int( f'{y}{y}{x}{x}', p ) )
      except:
        pass



