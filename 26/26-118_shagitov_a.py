# Автор: М. Шагитов

with open('26-118.txt') as file:
    t, n, m = map(int, file.readline().split())
    sellers_info = {}
    for line in file:
        seller_data = tuple(map(int, line.split()))
        sellers_info[seller_data] = seller_data[2]
    purchase_counts = {key: 0 for key in sellers_info}

    for period in range(1441 // t + 1):
        current_minute = period * t
        available_sellers = [(seller, sellers_info[seller]) for seller in sellers_info if seller[0] <= current_minute <= seller[1] and seller[2] < m]

        if (chosen_seller := min(available_sellers, key=lambda x: (x[1], -x[0][1]), default=None)) is not None:
            sellers_info[chosen_seller[0]] += 1
            purchase_counts[chosen_seller[0]] += 1

    top_seller = max(purchase_counts, key=lambda x: purchase_counts[x])
    print(top_seller[1] - top_seller[0] + 1, purchase_counts[top_seller])