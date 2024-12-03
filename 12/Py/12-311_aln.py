#12.311_Aвтор_А.Л.Наймушин

k = m = 200
for n in range(100,201):
  s = '>' + k*'1' + m*'2' + n*'0'
  while '>1' in s or '>2' in s or '>0' in s:
    if '>1' in s:
      s = s.replace('>1', '20>', 1)
    if '>2' in s:
      s = s.replace('>2', '00>', 1)
    if '>0' in s:
      s = s.replace('>0', '10>', 1)
  su = sum(int(x) for x in s if x in '0123456789')
  if su == 599:
    print(n)
    break
'''
Rez = 199
'''
