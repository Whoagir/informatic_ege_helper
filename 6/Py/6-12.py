# Автор: А. Носкин

k = 0 # кол-во точек
for x in range(300):
    for y in range(300):
        if 0 < x < 50 and 150 < y < 200:
            k+=1
print(k)


