# Автор: А. Куканова

count = 0
for x in range(8 ** 3, 8 ** 4):
    if x % 4 == 0:
        count += 1
print(count)