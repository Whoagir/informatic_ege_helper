# Логическая функция F задаётся выражением (x ∨ y) → (z ≡ x).
#
# Дан частично заполненный фрагмент, содержащий неповторяющиеся строки таблицы истинности функции F.
#
# Определите, какому столбцу таблицы истинности соответствует каждая из переменных x, y, z
print('x y z ')
a=[True,False]
for x in a:
    for y in a:
        for z in a:
            f=(x or y) <= (z==x)
            if f==0:
                print(int(x),int(y),int(z))
#Ответ xzy