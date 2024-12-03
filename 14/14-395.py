import string

A = string.digits + string.ascii_uppercase

for p in range(2, 37):
  for x in A[1:p]:
    sx = f'89{x}0'
    sy = f'{x}6{x}4'
    for y in A[1:p]:
      ss = f'1{y}{y}14'
      try:
        if int( sx, p ) + int( sy, p) == int( ss, p ):
          print( x, y, p )
          print( int( f'{y}{x}{y}{x}', p ) )
          found = True
      except:
        pass



