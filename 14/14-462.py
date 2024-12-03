# Автор: PRO100-ЕГЭ

for x in range(12):
  n = int(f'9A87{x:x}21', 12) + int(f'2{x:x}68', 14) - int(f'1{x:x}2F4', 16)
  if n % 3 == 0:
    print( x, n // 3 )

