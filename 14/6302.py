for p in range(9, 50):
    for x in range(p):
        for y in range(p):
            for z in range(p):
                if ((y * (p ** 2)) + (3 * p) + y) + ((y * (p ** 2)) + (6 * p) + 5) == (x * (p ** 3) + (2 * (p ** 2)) + (z * p) + 0):
                    print((x * (p ** 2)) + y * p + z, p)