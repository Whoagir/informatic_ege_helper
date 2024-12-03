f=open('17-243.txt')
a=[int(e)   for e in f  ]
b=[]
c=[]
for i in range (len (a)):
 if a[ i]%107==0:
     b.append(a[ i])
cymma=max(b)
for i in range (len (a)-1):
 s=''
 v=a[ i]
 while v!=0:
     s=str(v%7)+s
     v=v//7
 s1=''
 v1=a[i+1]
 while v1!=0:
     s1=str(v1%7)+s1
     v1=v1//7
 print(a[i], s, a[i+1], s1)

 if ((a[ i]>cymma ) or (a[i+1]>cymma )) and (s.count('36')>0 or s1.count('36')>0) :
         c.append(a[ i]+a[i+1])
print(len(c),min(c))