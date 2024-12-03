# Автор: М. Ишимов

for x in '0123456789ABCDEFGHIJK':
  s = int(f'3{x}41', 21) + int(f'684132{x}5', 21) + int(f'9918{x}', 21) + int(f'73{x}7{x}23', 21) + int(f'21669{x}1{x}', 21)
  if s % 20 == 0:
      print(x, s // 20)
