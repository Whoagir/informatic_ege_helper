# Автор: А. Богданов

for x in range(10):
  a = 1 * int(f'123{x}5') + 5
  b = 1 * int(f'1{x}233') + 5
  if (a+b) % 14 == 0:
    r = (a+b) // 14

print(r)

for x in range(10):
  s = 1*(12304+x*10)+5 + 1*(10233+x*1000)+5
  if s % 14 == 0:
    r = s // 14

print(r)