# Автор: А. Носкин

# алфавит 15сс
s = "0123456789abcde"
# алфавит 17сс
s1 = "0123456789abcdefg"
Ymin = 17
for x in s:
    for y in s1:
        a1 = "123" + x + "5"
        a2 = "67" + y + "9"
        summ = int(a1,15) + int(a2,17)
        if  summ % 131 == 0 and int(y,17)<Ymin :
            otvet = summ // 131 # перезаписали
            Ymin = int(y,17)
print(otvet)
            

