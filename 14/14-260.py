# Михлин Б.С.
'''
Число 609 записали в системах счисления с основаниями от 2 до 10 включительно.
При каких основаниях в записи этого числа крайние цифры (самая левая и самая правая) имеют разную четность?
Например, число 124 - подходит, а 123 - нет, т.к. цифры 1 и 3 имеют одинаковую четность (нечетные).
В ответе укажите сумму всех подходящих оснований.
Ответ: 36
'''
s=0
for x in range(2,11):
    n=609
    nx=''
    while n:
        nx=str(n%x)+nx
        n//=x
    for i in range(len(nx)-1):
        if int(nx[0])%2==int(nx[-1])%2:
            break
    else:
        s+=x
        #print(x,nx) # отладочная
print(s)  # Ответ: 36         