# Коротков Михаил Сергеевич
# https://vk.com/mskorotkov

file = open("26-81.txt")

N, K = map(int, file.readline().split())
a = []
for _ in range(N):
    floor, row, pos = map(int, file.readline().split())
    a.append((floor, row, pos))
    
a.sort()

rows = set()
for i in range(1, len(a)):
    floor1, row1, pos1 = a[i - 1]
    floor2, row2, pos2 = a[i]
    
    if (floor1 == floor2) and (row1 == row2) and (pos2 - pos1 >= 5):
        rows.add(row1)
       
print(max(rows), len(rows))
