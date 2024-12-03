# Автор: А. Богданов

for x in range(10):
  a = 1 * int(f'123{x}4') + 1
  b = 1 * int(f'1234{x}') + 1
  if (a+b) % 10 == 0:
    r = (a+b) // 10

print(r)

for x in range(10):
  s = 1*(12304+x*10)+1 + 1*(12340+x*1)+1
  if s % 10 == 0:
    r = s // 10

print(r)