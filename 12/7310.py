d=0
for a in range(1,31):
    for b in range(1,19):
        for c in range(1,19):
            if 2*b+2*c==36 and a+3*b+c==30:
                if a+b+c>d:
                    d=a+b+c
print(d)