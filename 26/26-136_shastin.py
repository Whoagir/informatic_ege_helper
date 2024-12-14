f = open('26-136.txt')
n, m = map(int, f.readline().split())
a = [list(map(int, x.split())) for x in f]

bought = sorted([x[0] for x in a if x[1] == 1])
k = s = mk1 = ms1 = mk2 = ms2 = v1 = v2 = last = 0
for x in bought:
    if k == 0 or last == x:
        k += 1
        s += x
    else:
        k, s = 1, x
    if x > m and k > mk1:
        mk1, ms1, v1 = k, s, x
    if x <= m and k > mk2:
        mk2, ms2, v2 = k, s, x
    last = x

print(ms1 + ms2, sum(x[0] in (v1, v2) and x[1] == 0 for x in a))

























'''
maxR = maxB = last = 0
minR = minE = 10e20
for i in range(n):
    s, e, c = colors[i]
    if c == 'R' and e > maxR:
        maxR = e
    elif c == 'B' and e > maxB:
        maxB = e
    if s > last + 1:
        maxR = maxB = 0
        minR = minE = 10e20
        if c == 'R':
            maxR, minR = s, e
        elif c == 'B':
            maxB, minB = s, e
    last = max(last, e)
    if maxR > maxB:
        curr_color = 'R'
        max_curr_color = maxR
    else:
        curr_color = 'B'
        max_curr_color = maxB
    max_uncurr_color = 0
    for j in range(i+1, n):
        s2, e2, c2 = colors[j]
        if s2 > max_curr_color + 1:
            break
        if c2 == curr_color:
            max_curr_color = max(max_curr_color, e2)

        if c2 != curr_color:
            max_uncurr_color = max(max_uncurr_color, e2)
            if s2
'''

















'''
# R G RG
# G R RG
# R RG G
# G RG R
# RG R G
# RG G R

endmaxover = 0
colorover = None
for i in range(n-1):
    start, end, color = colors[i]
    if color != colorover:
        if end > endmaxover:
            endmaxover = end
            colorover = color
        continue
    else:
        if colorover == None: colorover = color
        endmaxover = max(endmaxover, end)
    endmax = end
    flag = 1
    last_ind = None
    for j in range(i+1, n):
        startR, endR, colorR = colors[j]
        if startR > endmax:
            flag = 0
            break
        if colorR == color:
            endmax = max(endmax, endR)
        else:
            endRmax = endR
            last_ind = j
            for r in range(j+1, n):
                startR2, endR2, colorR2 = colors[r]
                if colorR2 == colorR:
                    if endR2 > endRmax:
                        last_ind = j
                    endRmax = max(endRmax, endR2)
                else:
                    break
            break
    if flag:
        if start < startR and endmax < endRmax:
            ml = min(ml, endmax + 1 - (startR - 1) + 1)
            if endmax + 1 - (startR - 1) + 1 == 13: print(startR-1, endmax + 1)
        elif start == startR and endmax != endRmax:
            startboard = None
            for j in range(i-1, -1, -1):
                if endL < start - 1:
                    break
                startL, endL, colorL = colors[j]
                if endmax > endRmax and colorL != color and startL <= start - 1:
                    startboard = start - 1
                    break
                elif endRmax > endmax and colorL != colorR and startL <= start - 1:
                    startboard = start - 1
            if startboard != None:
                ml = min(ml, min(endmax, endRmax) + 1 - startboard + 1)
        elif start != startR and endmax == endRmax and last_ind != None:
            endboard = None
            for j in range(last_ind+1, n):
                start2, end2, color2 = colors[j]
                if start2 > endmax:
                    break
                if start < startR and color2 != color:
                    endboard = endmax + 1
                    break
            if endboard != None:
                ml = min(ml, endboard - start + 1)

print(count, ml)
'''









'''
last_R_start = last_R_end = last_G_start = last_G_end = -10**30
for start, end, color in sorted(colors):
    if not (start <= max(last_R_end, last_G_end) + 1):
        count += 1
    if color == 'R':
        if start <= max(last_R_end, last_G_end) + 1:
            # определить максимальный отрезок
            pass
        last_R_start = start
        last_R_end = max(end, last_R_end)
    else:
        if start <= max(last_R_end, last_G_end) + 1:
            # определить максимальный отрезок
            pass
        last_G_start = start
        last_G_end = max(end, last_G_end)

print(count, ml)
'''






















'''
# 0 - R, 1 - B, 2 - RB
colors_line = [[0]*3 for _ in range(k+1)]

for start, end, color in colors:
    for km in range(start, end + 1):
        if color == 'R':
            colors_line[km][0] = 1
        if color == 'B':
            colors_line[km][1] = 1
        if sum(colors_line[km][:2]) == 2:
            colors_line[km][2] = 1
'''

'''
mn = k + 1
fl = [10**30]*3
lt = None
count = 0
for km in range(k+1):
    if colors_line[km][2]: fl[2] = km
    elif colors_line[km][0] and not colors_line[km][1]: fl[0] = km
    elif colors_line[km][1]: fl[1] = km
    else:
        if lt != km-1 and lt != None:
            count += 1
        lt = km
    if 10**30 not in fl:
        mn = min(mn, km+1 - min(fl))

print(count, mn)
'''



'''
mn = k + 1
for start in range(k + 1):
    for end in range(start + 1, k + 1):
        fl = [0]*3
        for km in range(start, end + 1):
            if colors_line[km][2]: fl[2] = 1
            elif colors_line[km][0] and not colors_line[km][1]: fl[0] = 1
            elif colors_line[km][1]: fl[1] = 1
        if 0 not in fl:
            mn = min(mn, end - start + 1)
'''
