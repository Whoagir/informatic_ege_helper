# Автор: А. Носкин

# алфавит 13сс
s = "0123456789abc"
# алфавит 22 сс не с 0, т.к число не начинается с "0"
s1 = "123456789" 
for i in range(12):# формируем алфавит 22СС
    s1 +=chr(ord("a")+i)

XYmin = 34
for x in s1:
    for y in s:
        a1 = x +"23" + x + "5"
        a2 = "67" + y + "9" + y
        razn = int(a1,22) - int(a2,13)
        if  razn % 57 == 0 and (int(x,22) + int(y,13))<XYmin :
            otvet = razn // 57 # перезаписали
            XYmin = int(x,22) + int(y,13)
print(otvet)            
            

