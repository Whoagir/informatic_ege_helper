import string

A = string.digits + string.ascii_uppercase

for p in range(2, 37):
  for x in A[1:p]:
    sx = f'87{x}6'
    sy = f'{x}5{x}8'
    for y in A[1:p]:
      ss = f'{y}7{y}92'
      try:
        if int( sx, p ) + int( sy, p) == int( ss, p ):
          print( x, y, p, int( ss, p ) )
          print( int( f'{y}{x}{x}{y}', p ) )
      except:
        pass



