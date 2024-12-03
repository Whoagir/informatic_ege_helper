
for x in '0123456789ABCDEF':
  n = int( f'8569{x}', 16 ) + int( f'12{x}48', 16 )
  s8 = f"{n:o}"
  kEven = sum( 1 for d in s8 if d in '0246' )
  if kEven <= 2:
    print( x, s8 )