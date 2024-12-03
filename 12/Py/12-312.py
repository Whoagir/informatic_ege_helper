for n in range(41,50):
  s = '>' + n*'0' + n*'1' + n*'2'
  while '>1' in s or '>2' in s or '>0' in s:
    if '>1' in s:
      s = s.replace('>1', '22>', 1)
    if '>2' in s:
      s = s.replace('>2', '00>', 1)
    if '>0' in s:
      s = s.replace('>0', '11>', 1)
  s = s.replace('>' ,'1' , 1)
  su = sum(int(x) for x in s if x in '0123456789')
  if su % 100 == 77:
    print(n)
    break