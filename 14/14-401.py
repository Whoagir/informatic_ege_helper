import string

A = string.digits + string.ascii_uppercase

for p in range(2, 37):
  for x in A[0:p]:
    sx = f'4{x}46'
    sy = f'{x}{x}17'
    for y in A[1:p]:
      ss = f'{y}386{y}'
      try:
        if int( sx, p ) + int( sy, p) == int( ss, p ):
          print( x, y, p )
          print( int( f'{x}{y}{x}{y}', p ) )
      except:
        pass



