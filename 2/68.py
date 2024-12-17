print('x y z w')
a=[True,False]
for x in a:
    for y in a:
        for z in a:
            for w in a:
                f=(not(y<=(x==w))) and(z<=x)
                if f==1:
                    print(int(x), int(y), int(x), int (w))
print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not(y <= (x == w)) and (z <= x):
                    print(x, y, z, w)