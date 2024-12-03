s2023 = 0
for n in range(10000, 100000):
  s = f'{n:o}'
  for _ in range(2):
    [s:=s.replace(c,'2') for c in '1357']
    s += str(n%8)
  R = int(s,8)
  if R % 2023 == 0:
    s2023 += n

print( s2023 )