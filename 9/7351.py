import csv
v=open('9-228.csv')
reader=csv.reader(v)
v1=0
for row in reader:
    s=row[0]
    a,b,c,d,e,f=map(int,s.split(';'))
    f1=(a!=b) and (a!=c) and (a!=d) and (a!=e) and (a!=f) and (b!=c) and (b!=d) and (b!=e) and (b!=f) and (c!=d) and (c!=e) and (c!=f) and (d!=e) and (d!=f) and (e!=f)
    f2=