# Автор В.Н. Шубинкин

from string import digits as d, ascii_uppercase as letters
digits = d + letters

for x in range(11):
    for y in range(11):
        x1 = '7' + digits[y] + '23' + digits[x] + '5'
        x2 = '67' + digits[x] + '9' + digits[y]
        res = int(x1, 25) + int(x2, 11)
        if res % 131 == 0:
            print(res // 131)




