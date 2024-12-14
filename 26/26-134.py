# Автор: Г. Шапошников

f=open("26-134.txt")

n,t=map(int,f.readline().split())

startTime=[0]*n
length=[0]*n
typePerson=[""]*n

for i in range(n):
    st,ln,typePerson[i]=f.readline().split()
    startTime[i]=int(st)
    length[i]=int(ln)

#Блок с сортировкой, можно пропустить,
#если сортировка осуществлялась в Excel
#с последующим сохранением в файл
#уже отсортированных данных
for i in range(n-1):
    for j in range(i+1,n):
        if(startTime[i]>startTime[j]):
            p=startTime[i]
            startTime[i]=startTime[j]
            startTime[j]=p
            p=length[i]
            length[i]=length[j]
            length[j]=p
            p=typePerson[i]
            typePerson[i]=typePerson[j]
            typePerson[j]=p


queueMan=[]
queueWoman=[]
queueOldman=[]

cm=0
cw=0
co=0
lastTypePerson=""
nextPerson=0
timeBusy=0

for time in range(1,t+1):
    while(nextPerson<n and startTime[nextPerson]==time):
        if(typePerson[nextPerson]=="M"):
            queueMan.append(length[nextPerson])
        if(typePerson[nextPerson]=="W"):
            queueWoman.append(length[nextPerson])
        if(typePerson[nextPerson]=="G"):
            queueOldman.append(length[nextPerson])
        nextPerson+=1
    timeBusy-=1
    if(timeBusy<=0):
        if(len(queueOldman)>0):
            timeBusy=queueOldman[0]
            co+=1
            lastTypePerson="G"
            queueOldman.remove(queueOldman[0])
        elif(len(queueWoman)>0):
            timeBusy=queueWoman[0]
            cw+=1
            lastTypePerson="W"
            queueWoman.remove(queueWoman[0])
        elif(len(queueMan)>0):
            timeBusy=queueMan[0]
            cm+=1
            lastTypePerson="M"
            queueMan.remove(queueMan[0])

if(lastTypePerson=="G"):
    r=co
elif(lastTypePerson=="W"):
    r=cw
else:
    r=cm

print(co+cm+cw,r)
