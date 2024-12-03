# Автор: А. Носкин
# алфавит 15сс
s = "0123456789abcde"
for x in s:
    a1 = "82" + x + "19"
    a2 = "6" + x + "073"
    raz = int(a1,15) - int(a2,15)
    if  raz % 11 == 0:
            print(raz // 11)
            break


