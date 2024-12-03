from itertools import product

even = '0246'
odd = '1357'
count = 0
for s in product('01234567',repeat=8):
    s = ''.join(s)
    if s[0] != '0':
      for c in even: s = s.replace(c,'0')
      for c in odd: s = s.replace(c,'1')
      if s[0] == '1' and s[-1] == '1' and '00' in s and '000' not in s:
        count += 1

print(count)
