for x in range(10):
  base1 = int(f'12{x}34')
  base2 = int(f'124{x}3')
  a = 1*base1**2 + 0*base1 + 1
  b = 1*base2**2 + 1*base2 + 1
  if (a+b) % 30 == 0:
    r = (a+b) // 30

print(r)

for x in range(10):
  base1 = 12034 + x*100
  base2 = 12403 + x*10
  s = 1*base1**2 + 0*base1 + 1 + \
      1*base2**2 + 1*base2 + 1
  if s % 30 == 0:
    r = s // 30

print(r)