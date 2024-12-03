for x in range(10):
  base1 = int(f'123{x}4')
  base2 = int(f'124{x}3')
  a = 1*base1**2 + 1*base1 + 3
  b = 1*base2**2 + 2*base2 + 2
  if (a+b) % 10 == 0:
    r = (a+b) // 10

print(r)

for x in range(10):
  base1 = 12304 + x*10
  base2 = 12403 + x*10
  s = 1*base1**2 + 1*base1 + 3 + \
      1*base2**2 + 2*base2 + 2
  if s % 10 == 0:
    r = s // 10

print(r)