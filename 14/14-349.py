# Автор: А. Носкин
# алфавит 19сс
s = "0123456789abcdefghi"
for x in s:
    a1 = "55" + x + "36"
    a2 = x + "2724"
    summ = int(a1,19)+int(a2,19)
    if summ%11==0:
        print(summ//11)
        break


