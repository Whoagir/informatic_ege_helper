c=0
for n in range(1,1000):
    s=bin(n)[2:]
    v=s.rfind('0')
    if s.count('0')==0:
        continue
    s1=s[:v]+s[:2]
    # print(s,s1)
    s2=s1[::-1]
    r=int(s2,2)
    if r==127:
        c+=1
print(c)