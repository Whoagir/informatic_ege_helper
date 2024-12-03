# Автор: А. Минак

def repaint(field, pos):
    field[pos] = not field[pos]

field = [False] * 10_000

pos = 0

for _ in range(4):
    repaint(field, pos)
    pos -= 2
    for _ in range(4):
        pos += 3
        repaint(field, pos)
    repaint(field, pos)

r = pos
k = sum(field)
print(r*k)
