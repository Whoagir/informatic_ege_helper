k = m = 200
for n in range(100,201):
  s = '>' + k*'1' + m*'2' + n*'*'
  while '>1' in s or '>2' in s or '>*' in s:
    if '>1' in s:
      s = s.replace('>1', '111>', 1)
    if '>2' in s:
      s = s.replace('>2', '1>', 1)
    if '>*' in s:
      s = s.replace('>*', '%2*>', 1)
  su = sum(int(x) for x in s if x in '0123456789')
  if su == 1190:
    print(n)
    break