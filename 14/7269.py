c = []
for x in range(57):
    for y in range(57):
        t = 5*57**7+x*57**6+2*57**5+7*57**4+y*57**3+3*57**2+2*57**1+y
        if t % 56 == 0:
            print(x*57**1+y)