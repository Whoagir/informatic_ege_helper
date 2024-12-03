# Автор: А. Куканова

count = 0

even = '0246'
for x in range(8 ** 3, 8 ** 4):
    oct_x = oct(x)[2:]
    if oct_x[0] in even and all(oct_x[i] >= oct_x[i + 1] for i in range(3)):
        count += 1
print(count)


# Автор: Н. Гаязова

from itertools import *

w = set()
for s in product('01234567',repeat = 4):
  s = ''.join(s)
  if s[0] in '246' and s[0]>=s[1]>=s[2]>=s[3]: w.add(s)

print(w)
print(len(w))