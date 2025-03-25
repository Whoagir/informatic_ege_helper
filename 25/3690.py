dev=[]
for y in range(1, 10):
    s1 = str(y) + '2'
    dev.append(int(s1))
for x in range(0,10):
    for x1 in range(0,10):
        for x2 in range(0,10):
            for x3 in range(0,10):
                s='1'+str(x)+'3'+str(x1)+'5'+str(x2)+'6'+str(x3)+'8'
                c=0
                for i in range(len(dev)):
                    if int(s)% int(dev[i])==0:
                        c+=1
                    if c>=len(dev)/2:
                        print(s,int(s)//min(dev))
print(len(dev))