# Автор: А. Богданов

for x in range(10):
  a = 1 * int(f'1{x}234') + 3
  b = 1 * int(f'{x}1234') + 3
  if (a+b) % 13 == 0:
    r = (a+b) // 13

print(r)

for x in range(10):
  s = 1*(10234+x*1000)+3 + 1*(1234+x*10000)+3
  if s % 13 == 0:
    r = s // 13

print(r)