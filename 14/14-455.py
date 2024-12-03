# Автор: М. Ишимов

for x in '0123456789ABCDEFGHIJK':
  s = int(f'8G{x}I2', 21) + int(f'6EI{x}FC3', 21) + int(f'455E{x}', 21) + int(f'D5H{x}95596', 21) + int(f'KE7{x}', 21) + int(f'8CG{x}33E6', 21)
  if s % 20 == 0:
      print(x, s // 20)
