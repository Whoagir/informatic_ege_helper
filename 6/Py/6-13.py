# Автор: А. Носкин

k = 100 # кол-во точек до квадрата (от у=0 до у=99)
for x in range(200):
    for y in range(300):
        if 0 <= x <= 100 and 100 <= y <= 200:
            k+=1
print(k)