# 306)	*(Д. Статный) Григорий придумывает 16-буквенные слова,
# состоящие из букв слова АНТИУТОПИЯ. Сколько слов, содержащих
# комбинацию АНТИУТОПИЯ, может составить Григорий, если справа
# от этой комбинации находятся только согласные в алфавитном
# порядке, а слева от нее – гласные в обратном алфавитном порядке?
# Буквы в словах могут повторяться любое количество раз или же не встречаться вовсе.
#Mufazzalov
import itertools

ans = 0
for ksog in range(1, 6):
    for j in itertools.combinations_with_replacement('НПТ', ksog):
        ans += len(list(itertools.combinations_with_replacement('АИОУЯ', 6 - ksog)))
print(ans)