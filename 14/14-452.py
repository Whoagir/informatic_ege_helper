# Автор: М. Ишимов

for x in '0123456789ABCDEFGHIJKLMNO':
  s = int(f'2{x}{x}26129', 25) + int(f'54{x}{x}{x}711', 25)
  if s % 24 == 0:
      print(x, s // 24)
