f = open('26main.txt')
n, start, finish = [int(x) for x in f.readline().split()]
a = []
for i in range(n):
    l, r = [int(x) for x in f.readline().split()]
    a.append([l, r])

a.sort()
end = start
t = -1000
count = 0
first_teacher = -1
for otr in a:
    l = otr[0]
    r = otr[1]
    if l <= end:
        t = max(t, r)
    else:
        if count == 0:
            first_teacher = t
        count += 1
        end = t
        t = max(end, r)
        
    if t >= finish:
        count += 1
        break
       
print(count, first_teacher - start)
#Видеоразбор
# https://youtu.be/y7N-5jX99X0?t=14195