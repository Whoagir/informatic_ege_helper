import string

A = string.digits + string.ascii_uppercase

for p in range(2, 37):
  for x in A[0:p]:
    sx = f'34{x}5'
    sy = f'{x}9{x}3'
    for y in A[1:p]:
      ss = f'{y}{y}68'
      try:
        if int( sx, p ) + int( sy, p) == int( ss, p ):
          print( x, y, p )
          print( int( f'{y}{x}{x}{y}', p ) )
      except:
        pass

