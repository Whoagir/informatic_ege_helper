# Автор: И. Карпачев

f = open('26-149.txt')

# 1 подъезд 1 - 40
#  1й этаж: 1 - 8; 2й этаж: 9 - 16; ... 5й этаж: 33 - 40
# 2 подъезд 41 - 80
# 3 подъезд 81 - 120
# ..................
# 9 подъезд 321 - 360

# def get(flat: int) -> tuple (подъезд, этаж)
def get(flat: int) -> tuple:
    # номер подъезда
    porch = (flat - 1) // 40 + 1
    # этаж
    floor = ((flat - (porch - 1) * 40) - 1) // 8 + 1
    return (porch, floor)

n = int(f.readline())

box = []

for _ in range(n):
    home, flat = map(int, f.readline().split())
    box.append((home, flat))

f.close()

box.sort()

ans1 = 0
ans2 = 0
for i in range(1, n):
    # проверка на совпадение номеров дома
    if box[i][0] == box[i - 1][0]:
        data1 = get(box[i - 1][1])
        data2 = get(box[i][1])
        if data1[0] == data2[0] and data1[1] == data2[1]:
            ans1 = box[i][0]
            break

for i in range(1, n):
    # проверка на совпадение номеров дома
    if box[i][0] == box[i - 1][0]:
        data1 = get(box[i - 1][1])
        data2 = get(box[i][1])
        if box[i][0] == ans1:
            ans2 = box[i][1]

print(ans1, ans2)
