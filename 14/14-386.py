
for x in '0123456789ABCDEFG':
  n = int( f"10{x}0", 17 ) + int( f"F0{x}FF", 17 )
  if n % 13 == 0:
    print( x, n // 13 )