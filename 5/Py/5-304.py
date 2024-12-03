def sumHexDigits( s ):
  res = sum( int(x,16) for x in s )
  return res

n = 1
while True:
  s = f"{n:X}" + ('F' if n % 2 == 0 else '0')
  for _ in range(2):
    s += f"{sumHexDigits(s) % 16:X}"
  if s.count(min(s)) == 5*s.count(max(s)):
    print( n, s )
    break
  n += 1


# Автор: Е. Усов

for n in range (1,10000):
    s=hex(n)[2:]
    if n%2==0: s+='f'
    else: s+='0'
    valid=[hex(i)[2:] for i in range (0,16)]
    sNum=0
    for i in range (2):
        for j in range (len(s)):
            sNum+=valid.index(s[j])
        s+=hex(sNum%16)[2:]
    d=dict()
    for i in range (len(s)):
        if s[i] in d: d[s[i]]+=1
        else: d[s[i]]=1
    dList=sorted(list(d.items()), key=lambda x: x[0])[::-1]
    if dList[0][1]*5==dList[-1][1]:
        print(n)
        break

