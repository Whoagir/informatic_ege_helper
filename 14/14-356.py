# Автор В.Н. Шубинкин

from string import digits as d, ascii_uppercase as letters
digits = d + letters

for x in range(14, -1, -1):
        x1 = '131' + digits[x] + '1'
        x2 = '13' + digits[x] + '3'
        res = int(x1, 15) + int(x2, 17)
        if res % 11 == 0:
            print(res // 11)
            break




