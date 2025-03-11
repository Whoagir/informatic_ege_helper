def pr(n):
    for i in range(2,int(n**(1/2))+1):
        if n%i==0:
            return False
    return True
for n in range(3614033,3614116):
    if pr(n):
        print(n)