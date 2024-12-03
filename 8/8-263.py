from itertools import product

count = 0
for d in product('012345678', repeat=5):
  s = ''.join(d)
  if s[0] not in '01357' and s[-1] not in '18' and \
     s.count('3') <= 1:
     count += 1

print( count )

# Автор: Михлин Б.С.

n = 0
for x in range(9**4, 9**5):
    d = x // 9**4
    if d % 2 == 0 and 1 != x % 9 != 8:
        xx = x
        k = 0
        while xx:
            if xx % 9 == 3:
                k += 1
                if k > 1:
                    break
            xx //= 9
        else:
            n += 1
print(n)  # Ответ: 18944

# Автор: Михлин Б.С.

n = 0
ch = '02468'
for x in range(9**4, 9**5):
    s = ''
    while x:
        s = str(x % 9) + s
        x //= 9
    if s[0] in ch and '1' != s[-1] != '8' and s.count('3') < 2:
    # if int(s[0]) % 2 == 0 and '1' != s[-1] != '8' and s.count('3') < 2:
            n += 1
print(n)  # Ответ: 18944
