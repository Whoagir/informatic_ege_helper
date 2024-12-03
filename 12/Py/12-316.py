# Автор: А. Рогов

for k in range(1, 1000):
  s = '>' + '1' * 22 + '2' * k + '3' * 23
  while '>1' in s or '>2' in s or '>3' in s:
    if '>1' in s:
      s = s.replace('>1', '2>', 1)
    if '>2' in s:
      s = s.replace('>2', '21>', 1)
    if '>3' in s:
      s = s.replace('>3', '11>', 1)
  summ = sum(int(i) for i in s[:-1])
  if summ > 2023:
    print(k, summ)
    break


# Ответ: 645
