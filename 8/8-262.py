from itertools import product

digits8 = '01234567'
digits8x = '1234567'
even = ' 024'

count = 0
for d4 in digits8x:
  for d3, d2, d1, d0 in product(digits8, repeat=4):
    s = f' {d4}{d3}{d2}{d1}{d0} '
    if s.count('6') == 1:
      pos6 = s.index('6')
      if s[pos6-1] in even and s[pos6+1] in even:
        count += 1

print( count )

# Автор: А. Кабанов

w = ['16', '36', '56', '76', '61', '63', '65', '67']
count = 0
for x in product('01234567', repeat=5):
  s =''.join(x)
  if s[0] != '0' and s.count('6') == 1 and all(sub not in s for sub in w):
    count += 1
print( count )

# Автор: Михлин Б.С.

n = 0
for x in range(8**4, 8**5):
# for x in range(0o10_000,0o77_777+1):
    x8 = oct(x)
    if (x8.count('6') == 1 and
        '16' not in x8 and '36' not in x8 and '56' not in x8 and '76' not in x8 and
        '61' not in x8 and '63' not in x8 and '65' not in x8 and '67' not in x8):
        n += 1
print(n)  # Ответ: 2961

