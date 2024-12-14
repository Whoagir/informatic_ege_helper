
TARGET, LIMIT = 91, 110
ADD, MUL = 1, 2
N1 = 40

def nextMoves(x, y):
  return [ gameResult(x+ADD, y), gameResult(x*MUL, y),
           gameResult(x, y+ADD), gameResult(x, y*MUL) ]

def gameOver(x, y):
  if TARGET <= x+y:
    if x+y <= LIMIT:
        return 1
    else:
        return -1
  else: return 0

mem = {}
def gameResult(x, y):
  if (x,y) in mem: return mem[(x,y)]
  finish = gameOver(x,y)
  if finish == 1: return 0
  elif finish == -1: return 1
  nextCodes = nextMoves(x, y)
  negative = [c for c in nextCodes if c <= 0]
  if negative:
    res = -max(negative) + 1
  else:
    res = -max(nextCodes)
  mem[(x,y)] = res
  return res

ans1, ans2, ans3 = [], [], []
for S in range(50,0,-1):
  res = gameResult(N1, S)
  print( f"{S}: {res}" )
  if res == -1: ans1.append(S)
  if res == 2: ans2.append(S)
  if res == -2: ans3.append(S)

print( f"19: {sorted(ans1)}" )
print( f"20: {sorted(ans2)}" )
print( f"21: {sorted(ans3)}" )
