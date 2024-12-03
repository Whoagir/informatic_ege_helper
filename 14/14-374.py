for x in range(10):
  base1 = int(f'1{x}234')
  base2 = int(f'1{x}243')
  a = 1*base1**2 + 1*base1 + 2
  b = 1*base2**2 + 1*base2 + 1
  if (a+b) % 15 == 0:
    r = (a+b) // 15

print(r)

for x in range(10):
  base1 = 10234 + x*1000
  base2 = 10243 + x*1000
  s = 1*base1**2 + 1*base1 + 1 + \
      1*base2**2 + 1*base2 + 1
  if s % 15 == 0:
    r = s // 15

print(r)