# 14.302
# Автор: А.Л. Наймушин
x = 6**203 + 5*(6**405) - 3*(6**144) + 76 
#print(x)
sum = 0
while (x != 0):
    sum = sum + x % 6
    x = x // 6
    
print("Сумма цифр числа равна: ", sum)


'''
Rez = 304
'''
