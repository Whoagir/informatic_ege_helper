for x in range(10):
  b = 28
  a = 2*int(f'1{x}324') + 7
  c = sum( d*bn for d, bn in
          zip( (1, x, 3, 4, 2),
               (b**4, b**3, b**2, b, 1) ) )
  if (c - a) % 25 == 0:
    r = (c - a) // 25

print(r)

for x in range(10):
  b1 = 10324 + x*1000
  b2 = 28
  s = 1*b2**4 + 3*b2**3 + 4*b2**2 + x*b2 + 2  \
      - (2*b1 + 7)
  if s % 25 == 0:
    r = s // 25

print(r)