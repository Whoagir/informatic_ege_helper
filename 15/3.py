l=[]
p = list(range(20, 51))
q = list(range(30, 66))
for an in range(15, 70):
    for ae in range(an+1, 70):
        a = list(range(an, ae))
        f = True
        for x in range(1, 100):
            j = (not (x in a)) <= ((x in p) <= (not (x in q)))
            if not j:
                f=False
                break
        if f:
            l.append(ae-an)
print(min(l)-1)