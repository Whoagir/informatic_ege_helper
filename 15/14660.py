p=list(range(16,85))
q=list(range(27,43))
a=list(range(0,100))
for x in range(0,100):
    if (((x in a)<=(x in p)) or (x in q)) == False:
        a.remove(x)
print(a)
print(84-16)