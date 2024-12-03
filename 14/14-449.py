# Автор: М. Ишимов

for x in '0123456789ABCDEF':
  s = int(f'3BB{x}8', 16) + int(f'B67A{x}FE62', 16) + int(f'BEA2{x}D49B', 16) + int(f'8D7D{x}', 16)
  if s % 15 == 0:
      print(x, s // 15)

