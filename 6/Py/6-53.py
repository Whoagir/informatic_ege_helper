c = (2 * 250**2) ** 0.5
k = 0
for x in range(-400, 400):
    for y in range(-400, 400):
        if y < -x:
            if y < x:
                if y > x - c:
                    if y > -x - c:
                        k += 1
print(k)
