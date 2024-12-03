# Автор: М. Ишимов

for x in '0123456789ABCDEFGHIJKLMNOPQ':
  s = int(f'3616465{x}', 27) + int(f'99{x}95{x}69', 27)
  if s % 26 == 0:
      print(x, s // 26)

