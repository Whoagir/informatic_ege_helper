def F(n):
    if n<=400:
        return 1
    if n>400:
        return F(n-1)*(n-400)
print(F(701)/F(697))