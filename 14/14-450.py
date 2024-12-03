# Автор: М. Ишимов

for x in '0123456789ABCDEFG':
   for y in '0123456789ABCDEFG':
       s = int(f'7{x}589{y}', 17) + int(f'EE{x}{y}9AC', 17)
       if s % 13 != 0:
           break
   else:
       y = 3
       s = int(f'7{x}589{y}', 17) + int(f'EE{x}{y}9AC', 17)
       print(x, s // 13)
