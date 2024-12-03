#5.272 автор А.Л.Наймушин

def alg (x):
    x2 = x//2
    s = hex(x2)[2:]
    if x%4 != 0:
        s1 = 'F' + s + 'A0'
    else:
            s1 = '15' + s + 'C' 
    return s1

for x in range(1000,1, -1):
  R = int(alg(x),16)
  if R < 65536:
    print(x)
    break
'''
N = 31

'''        


   


