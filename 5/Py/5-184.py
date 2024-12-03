def alg( x ):
  s = "{:08b}".format(x-1)
  s1 = ""
  for c in reversed(s):
    if c == '1': s1 = '0' + s1
    else:        s1 = '1' + s1
  return int(s1,2)

for i in range(1, 256):
  #print( i, alg(i) )
  if alg(i) == 18:
    print(i)
    break

# 2 способ. Автор: А. Козлов
for i in range(1, 256):
  s = "{:08b}".format(i-1)
  s = s.replace('1', '2')
  s = s.replace('0', '1')
  s = s.replace('2', '0')
  if int(s,2) == 18:
    print( i )
