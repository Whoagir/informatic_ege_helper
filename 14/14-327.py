x = 18**105 + 25*16**100 - 3**51
h = f"{x:X}"
print(h)
for d in 'FEDCBA9876543210':
  c = h.count(d)
  if c > 0:
    print( d, c )
    break