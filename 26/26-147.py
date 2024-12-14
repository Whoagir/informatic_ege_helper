# Автор: И. Карпачев

f = open("26-147.txt")
n = int(f.readline())
box = []
personal = [0]
ans2 = 0
for i in range(n):
    a, b = map(int, f.readline().split())
    box.append((a, a + b))
f.close()

box.sort()

for i in range(n):
    st, et = box[i]
    for j in range(len(personal)):
        if st >= personal[j]:
            personal[j] = et
            if j == 0:
                ans2 += 1
            break
    else:
        personal.append(et)

print(len(personal), ans2)
