l=[]
p = list(range(130, 171))
q = list(range(150, 186))
for an in range(100, 200):
    for ae in range(an + 1, 200):
        a = list(range(an, ae))
        f = True
        for x in range(0, 200):
            j = (x in p) <= (((x in q) and (not (x in a))) <= (not (x in p)))
            if not j:
                f=False
                break
        if f:
            l.append(ae-an)
print(min(l))