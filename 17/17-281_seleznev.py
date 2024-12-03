def arif(x, y, z):
    if y == (x+z)//2 and y > x:
        return True
    return False


def geom(x, y, z):
    if y == int((x * z) ** 0.5) and z//y > 1:
        return True
    return False


def raz(x, y, z, w, e, f):
    if (arif(x, y, z) and geom(w, e, f) and (z-y == f//e)) or (geom(x, y, z) and arif(w, e, f) and (z//y == f-e)):
        return True
    return False

a = [int(x) for x in open('17-281.txt')]
cnt = 0
mx = 0
for i in range(len(a)-5):
    if (arif(a[i], a[i+1], a[i+2]) and geom(a[i+3], a[i+4], a[i+5])) or (geom(a[i], a[i+1], a[i+2]) and arif(a[i+3], a[i+4], a[i+5])):
        if raz(a[i], a[i+1], a[i+2], a[i+3], a[i+4], a[i+5]):
            cnt += 1
            mx = max(mx, sum([a[i], a[i+1], a[i+2], a[i+3], a[i+4], a[i+5]]))
print(cnt, mx)