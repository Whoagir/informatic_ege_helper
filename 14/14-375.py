for x in range(10):
  base1 = int(f'123{x}4')
  base2 = int(f'1{x}243')
  a = 1*base1**2 + 0*base1 + 1
  b = 1*base2**2 + 2*base2 + 3
  if (a+b) % 25 == 0:
    r = (a+b) // 25

print(r)

for x in range(10):
  base1 = 12304 + x*10
  base2 = 10243 + x*1000
  s = 1*base1**2 + 0*base1 + 1 + \
      1*base2**2 + 2*base2 + 3
  if s % 25 == 0:
    r = s // 25

print(r)