# Автор В.Н. Шубинкин

digits = '0123456789ABCDEFG'
pairs = {}
for x in range(15):
    for y in range(17):
        x1 = '123' + digits[x] + '5'
        x2 = '67' + digits[y] + '9'
        res = int(x1, 15) + int(x2, 17)
        if res % 131 == 0:
            pairs[(x, y)] = res // 131
pair_min_y = min(pairs, key=lambda p: p[1])
print(pairs[pair_min_y])
