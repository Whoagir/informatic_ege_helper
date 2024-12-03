for x in range(10):
  b = 22
  a = 2*int(f'1{x}324') + 3
  c = sum( d*bn for d, bn in
          zip( (1, 3, 4, x, 2),
               (b**4, b**3, b**2, b, 1) ) )
  if abs(a - c) % 50 == 31:
    r = abs(a - c) // 50

print(r)

for x in range(10):
  b1 = 10324 + x*1000
  b2 = 22
  s = 1*b2**4 + 3*b2**3 + 4*b2**2 + x*b2 + 2  \
      - (2*b1 + 3)
  if abs(s) % 50 == 31:
    r = abs(s) // 50

print(r)