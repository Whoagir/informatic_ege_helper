# Автор: А. Богданов

for x in range(10):
  a = 1 * int(f'12{x}34') + 9
  b = 2 * int(f'1{x}234') + 1
  if (a+b) % 11 == 0:
    r = (a+b) // 11

print(r)

for x in range(10):
  s = 1*(12034+x*100)+9 + 2*(10234+x*1000)+1
  if s % 11 == 0:
    r = s // 11

print(r)