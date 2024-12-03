# Автор: М. Ишимов

for x in '0123456789ABCDE':
  s = int(f'9{x}AB3{x}6E', 15) + int(f'6B53{x}', 15) + int(f'935D{x}BA{x}', 15) + int(f'E7D{x}{x}66', 15) + int(f'D{x}E514', 15)
  if s % 14 == 0:
      print(x, s // 14)
