
n = 3
while True:
  s = '1'*(n // 3) + '2'*(n // 3) + '3'*(n // 3)
  while '21' in s or '31' in s or '32' in s:
    if '21' in s:
      s = s.replace('21', '12', 1)
    if '31' in s:
      s = s.replace('31', '13', 1)
    if '32' in s:
      s = s.replace('32', '23', 1)

  if len(s) >= 50 and s[49] == '2':
    print(s)
    print(n)
    break
  n += 3

# Ответ: 75