
for x in '0123456789ABCDEF':
  n = int( f"10{x}A", 16 ) + int( f"FF{x}78", 16 )
  if n % 19 == 0:
    print( x, n // 19 )