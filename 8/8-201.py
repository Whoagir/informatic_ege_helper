# Автор: А. Куканова

count = 0

for x in range(16 ** 4, 16 ** 5):
    hex_x = hex(x)[2:]
    if all(hex_x[i] <= hex_x[i + 1] for i in range(4)):
        count += 1
print(count)
