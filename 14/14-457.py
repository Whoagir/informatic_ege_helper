# Автор: М. Ишимов

for x in '0123456789ABCDEFGHIJK':
   for y in '0123456789ABCDEFGHIJK':
       s = int(f'G2BA{y}I{x}{x}', 21) + int(f'G{x}4{y}DFI', 21)
       if s % 7 != 0:
           break
   else:
       y = 6
       s = int(f'G2BA{y}I{x}{x}', 21) + int(f'G{x}4{y}DFI', 21)
       print(x, s // 7)
