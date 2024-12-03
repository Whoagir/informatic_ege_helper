for x in range(10):
  b = 24
  a = 1*int(f'1{x}324') + 4
  c = sum( d*bn for d, bn in
          zip( (1, 3, x, 4, 2),
               (b**4, b**3, b**2, b, 1) ) )
  if (a+c) % 10 == 0:
    r = (a+c) // 10

print(r)

for x in range(10):
  b1 = 10324 + x*1000
  b2 = 24
  s = 1*b1 + 4 + \
      1*b2**4 + 3*b2**3 + x*b2**2 + 4*b2 + 2
  if s % 10 == 0:
    r = s // 10

print(r)