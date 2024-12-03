# Автор: А. Богданов

for x in range(10):
  a = 1 * int(f'1234{x}') + 5
  b = 1 * int(f'12{x}34') + 5
  if (a+b) % 14 == 0:
    r = (a+b) // 14

print(r)

for x in range(10):
  s = 1*(12340+x*1)+5 + 1*(12034+x*100)+5
  if s % 14 == 0:
    r = s // 14

print(r)