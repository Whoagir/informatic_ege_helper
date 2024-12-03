# Автор: М. Ишимов

for x in '0123456789ABCDEFGHI':
  s = int(f'14626{x}7', 19) + int(f'14161769{x}', 19) + int(f'72{x}383', 19)
  if s % 18 == 0:
      print(x, s // 18)
