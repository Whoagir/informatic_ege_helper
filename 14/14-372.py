# Автор: А. Богданов

for x in range(10):
  a = 1 * int(f'12{x}34') + 9
  b = 2 * int(f'1234{x}') + 3
  if (a+b) % 10 == 0:
    r = (a+b) // 10

print(r)

for x in range(10):
  s = 1*(12034+x*100)+9 + 2*(12340+x)+3
  if s%10 == 0:
    r = s // 10

print(r)