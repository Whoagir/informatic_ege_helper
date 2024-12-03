# Автор: М. Ишимов

for x in '0123456789ABCDEFGHIJKLM':
   for y in '0123456789ABCDEFGHIJKLM':
       s = int(f'9IE3{y}{x}', 23) + int(f'J5{y}B{x}L1', 23)
       if s % 13 != 0:
           break
   else:
       y = 3
       s = int(f'9IE3{y}{x}', 23) + int(f'J5{y}B{x}L1', 23)
       print(x, s // 13)
