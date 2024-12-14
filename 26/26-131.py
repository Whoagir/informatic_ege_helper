# Автор: Е. Джобс

k, n = 2, 6
s = [[1,10],[11,25],[16,15],[21,25],[26,20],[31,10]]
with open('26-131.txt') as f:
    n, k = map(int, f.readline().split())
    s = []
    for _ in range(n):
        st, t = map(int, f.readline().split())
        s.append([st, t])

#        [0:k] - выгодная сторона
#        [k:2*k] - невыгодная сторона
market = [[0]*(2*k) for _ in range(4501)]
# сначала самые ранние и с большим временем аренды
s.sort(key=lambda x: (x[0], -x[1]))
# количество продавцов, нашедших свое место
cnt = 0
for st, t in s:
    # желаемое время начала аренды
    rent_time = st
    # нужно определить
    # 1. Есть ли свободный лоток и его минимальный номер
    # 2. Определить есть ли собирающийся продавец и мин.номер
    # нет номера -1, -1 - не нашли

    # Определяем минимальный номер свободного лотка
    free_id = -1
    for i in range(2*k):
        if market[st][i] == 0:
            free_id = i
            break

    # Определяем минимальный номер освобождающегося лотка
    q_id = -1
    for i in range(2*k):
        # если продавец собирается и никто еще не занял место за ним
        if market[st][i] == 2 and market[st+15][i] == 0:
            q_id = i
            break
    if free_id == q_id == -1:
        #print('miss')
        continue

    cnt += 1

    # Может быть два случая, когда обрабатываем ожидание сбора
    # 1. Нет свободного лотка и есть освобождающийся
    # 2. Свободный лоток на невыгодной стороне, а освобождающийся на выгодной
    if free_id == -1 or free_id >= k and 0 <= q_id < k:
        free_id = q_id
        # перебираем 16 минут с текущей, до тех пор,
        # пока не найдем свободное время
        for qt in range(st, st+15+1):
            # если время qt для этого лотка свободно
            if market[qt][free_id] == 0:
                # это и есть время начала аренды
                rent_time = qt
                break
    #print(rent_time, rent_time+t-1)
    # торгуем t минут, начиная с rent_time минуты
    for rt in range(rent_time, rent_time+t):
        market[rt][free_id] = 1
    # собираемся 15 минут, начиная с rent_time+t минуты
    for rt in range(rent_time+t, rent_time+t+15):
        market[rt][free_id] = 2

k_cnt = 0
for t in range(4501):
    # если заняты все выгодные лотки
    if all(x > 0 for x in market[t][:k]):
        k_cnt += 1

print(cnt, k_cnt)
