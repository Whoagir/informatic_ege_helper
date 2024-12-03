for x in range(10):
  base1 = int(f'123{x}4')
  base2 = int(f'12{x}43')
  a = 1*base1**2 + 0*base1 + 3
  b = 1*base2**2 + 0*base2 + 2
  if (a+b) % 50 == 0:
    r = (a+b) // 50

print(r)

for x in range(10):
  base1 = 12304 + x*10
  base2 = 12043 + x*100
  s = 1*base1**2 + 0*base1 + 3 + \
      1*base2**2 + 0*base2 + 2
  if s % 50 == 0:
    r = s // 50

print(r)