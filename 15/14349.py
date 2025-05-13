s=[]
for a1 in range(1,200):
    for a2 in range(a1+1,200):
        fl=True
        for x in range(1,200):
            if not((78<=x<=151)<=(((54<=x<=120) and (not (a1<=x<=a2)))<=(not(78<=x<=151)))):
                fl=False
                break
        if fl:
            s.append(a2-a1)
print(min(s))