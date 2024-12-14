# Автор: Л. Шастин

f = open('26-138.txt')
n = int(f.readline())
k = int(f.readline())
m = int(f.readline())
bags = sorted(int(x) for x in f)
storages = {number: 0 for number in range(1, k + 1)}
for storage_number in range(1, k + 1):
    while bags:
        if storages[storage_number] + bags[-1] <= m:
            storages[storage_number] += bags[-1]
            bags.pop(-1)
        elif storages[storage_number] + bags[0] <= m:
            storages[storage_number] += bags[0]
            bags.pop(0)
        else:
            break
    if not bags:
        print(storage_number, m - storages[storage_number])
        break
