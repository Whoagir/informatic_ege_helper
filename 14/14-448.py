# Автор: М. Ишимов

for x in '0123456789ABCDEFGHIJKLMNOPQRSTU':
  s = int(f'DM5J{x}', 31) + int(f'D1MPJF{x}2P', 31) + int(f'I{x}57SE4K', 31) + int(f'JPEP{x}BB', 31) + int(f'CF2{x}13', 31)
  if s % 30 == 0:
      print(x, s // 30)

