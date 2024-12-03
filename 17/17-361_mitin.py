# Автор: И. Митин

def f(a,b,c):
    if a == b == c or (a != b and a != c and b != c):
        return 0
    if a == b:
        return c
    elif a == c:
        return b
    else:
        return a

def is_difference(a,b,c):
    if a == b == c or (a != b and a != c and b != c):
        return 0
    if a == b:
        return 1
    elif a == c:
        return 1
    else:
        return 1


a = [int(x) for x in open("17-361.txt")]
mn = min([int(x) for x in a if abs(x)%100==40])


ans = []
for i in range(len(a)-2):
    if is_difference(a[i],a[i+1],a[i+2]) and min(a[i],a[i+1],a[i+2]) > mn:
        n = f(a[i],a[i+1],a[i+2])
        if n == a[i]:
            ans.append(i+1)
        if n == a[i+1]:
            ans.append(i+2)
        if n == a[i+2]:
            ans.append(i+3)

print(len(ans),max(ans))
