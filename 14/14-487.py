s = "0123456789ABCDEFGHI"
for x in range(19):
  n = int( f"98897{s[x]}21", 19 ) + int( f"2{s[x]}923", 19 )
  if n % 18 == 0:
    print( x, n // 18 )