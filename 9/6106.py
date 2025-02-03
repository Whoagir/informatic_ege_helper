import csv
v=open('9-190.csv')
reader=csv.reader(v)
v1=0
for row in reader:
    s=row[0]
    a,b,c,d,e,f=map(int,s.split(';'))
    f1= ((a==b)or(a==c) or (a==d) or (a==e) or (a==f) or (b==c) or (b==d) or (b==e) or (b==f) or (c==d) or (c==e) or (c==f) or (d==e) or (d==f) or (e==f))
    f2=(((int(a%2)==1)+(int(b%2)==1)+(int(c%2)==1)+(int(d%2)==1)+(int(e%2)==1)+(int(f%2)==1))==3)
    if (f1 and (not(f2))) or ((not(f1)) and f2):
        v1+=1
        print(a,b,c,d,e,f,f1,f2,type(a),(a==b),(a==c),(a==d),(a==e),(a==f),(b==c),(b==d),(b==e),(b==f),(c==d),(c==e),(c==f),(d==e),(d==f),(e==f))
print(v1)