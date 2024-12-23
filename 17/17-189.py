'''
Михлин Б.С.
17.189 (П. Волгин) В файле 17-7.txt содержится последовательность целых чисел.
Элементы последовательности могут принимать значения от 0 до 200 включительно.
Определите сначала количество троек элементов последовательности,
в которых хотя бы одно число в троичной системе счисления в нулевом разряде имеет 2,
а затем сумму минимальных чисел из таких троек.
Под тройкой подразумевается три идущих подряд элемента последовательности.
'''
f = open('17-7.txt')
a = [int(x) for x in f]
n = 0     # количество подходящих троек чисел
s = 0     # сумма минимальных чисел из подходящих троек
for i in range(len(a) - 2):
    a3 = [a[i], a[i + 1], a[i + 2]]
    k = 0  # количество чисел в тройке с правой цифрой 2 в троичной системе
    for x in a3:
        if x % 3 == 2:
            k += 1
    if k > 0:
        n += 1
        s += min(a3)
print(n, s)  # Ответ: 91 2627
