for x in range(10):
  b = 19
  a = 2*int(f'13{x}24') + 6
  c = sum( d*bn for d, bn in
          zip( (1, 3, 4, x, 2),
               (b**4, b**3, b**2, b, 1) ) )
  if (a+c) % 15 == 0:
    r = (a+c) // 15

print(r)

for x in range(10):
  b1 = 13024 + x*100
  b2 = 19
  s = 2*b1 + 6 + \
      1*b2**4 + 3*b2**3 + 4*b2**2 + x*b2 + 2
  if s % 15 == 0:
    r = s // 15

print(r)