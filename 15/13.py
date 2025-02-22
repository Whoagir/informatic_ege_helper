p=[]
q=[]
c=0
for i in range(17,41):
    p.append(i)
for i1 in range(20,58):
    q.append(i1)
for amin in range(1,100):
    for amax in range(amin+1,100):
        a=[i for i in range(amin,amax)]
    for x in range(10,61):
        f=(not (x in a))<=(((x in p) and (x in q))<=(x in a))