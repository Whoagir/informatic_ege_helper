# Автор В.Н. Шубинкин

from string import digits as d, ascii_uppercase as letters
digits = d + letters

pairs = {}
for x in range(1, 22):
    for y in range(13):
        x1 = digits[x] + '23' + digits[x] + '5'
        x2 = '67' + digits[y] + '9' + digits[y]
        res = int(x1, 22) - int(x2, 13)
        if res % 57 == 0:
            pairs[(x, y)] = res // 57
pair_min_y = min(pairs, key=sum)
print(pairs[pair_min_y])
