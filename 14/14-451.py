# Автор: М. Ишимов

for x in '0123456789ABCDEFGHIJKLMNOPQRST':
   for y in '0123456789ABCDEFGHIJKLMNOPQRST':
       s = int(f'B{y}{x}6R94E{x}', 30) + int(f'M{y}KGN{x}', 30)
       if s % 10 != 0:
           break
   else:
       y = 4
       s = int(f'B{y}{x}6R94E{x}', 30) + int(f'M{y}KGN{x}', 30)
       print(x, s // 10)
