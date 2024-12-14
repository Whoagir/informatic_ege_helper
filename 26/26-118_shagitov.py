# Автор: М. Шагитов

from collections import defaultdict

with open('26-118.txt') as file:

    t, N, M = map(int, file.readline().split())
    buyer_purchases, previous_purchases, time_spent, results = defaultdict(set), {}, {}, {}

    for buyer_index, line in enumerate(file, 1):
        arrival, departure, prev_purchases = map(int, line.split())
        previous_purchases[buyer_index], results[buyer_index], time_spent[
            buyer_index] = prev_purchases, 0, departure - arrival
        buyer_purchases.update({minute: buyer_purchases[minute].union({buyer_index}) for minute in range(arrival, departure + 1, t)})

    for discount_minute in range(t, 1440, t):
        if (buyers := buyer_purchases[discount_minute]):
            winning_buyer = min(buyers, key=lambda x: (previous_purchases[x], -time_spent[x], int(previous_purchases[x] >= M)))
            if (updated_prev_purchases := (previous_purchases[winning_buyer] + 1)) <= M:
                previous_purchases[winning_buyer] = updated_prev_purchases
                results[winning_buyer] += 1

    winning_buyer_id, max_purchased_items = max(results.items(), key=lambda item: (item[1], previous_purchases[item[0]]))
    print(f"Total time spent in the store: {time_spent[winning_buyer_id] + 1}, Purchased items: {max_purchased_items}")
