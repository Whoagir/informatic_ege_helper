ans=[]
ans1=[]
for x in range(0,23):
    for y in range(0,23):
        s=int('5'+str(x)+str(x)+'78',17)+int('4'+str(x)+str(x)+'9',18)+int('88'+str(x)+str(x)+'5',19)+int('6'+str(x)+str(y)+'23',22)
        if s%405 and s>0:
            print(x,y)
            ans.append(x)
            ans1.append(y)
print(set(ans),set(ans1))