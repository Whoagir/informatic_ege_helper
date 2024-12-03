for x in range(10):
  b = 22
  a = 1*int(f'132{x}4') + 3
  c = sum( d*bn for d, bn in
          zip( (1, 3, x, 4, 2),
               (b**4, b**3, b**2, b, 1) ) )
  if abs(a - c) % 100 == 53:
    r = abs(a - c) // 100

print(r)

for x in range(10):
  b1 = 13204 + x*10
  b2 = 22
  s = 1*b2**4 + 3*b2**3 + x*b2**2 + 4*b2 + 2  \
      - (1*b1 + 3)
  if abs(s) % 100 == 53:
    r = abs(s) // 100

print(r)