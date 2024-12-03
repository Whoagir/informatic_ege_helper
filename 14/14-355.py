# Автор: А. Носкин
# алфавит 13сс
s = "0123456789abc"
for x in s:
    a1 = "8" + x + "121"
    a2 = "7" + x + "575"
    raz = int(a1,13) - int(a2,13)
    if  raz % 19 == 0:
            print(raz // 19)
            break


