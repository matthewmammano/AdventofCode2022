txt = open('text2.txt', 'r')
lines = txt.readlines()
lines = list(map(lambda i: i.split('\n'), lines))

lines2 = []
for i in lines:
    lines2 += [i[0]]
lines = lines2

lines = list(map(lambda i: i.split(' '), lines))

win = {'A': 'Y', 'B': 'Z', 'C': 'X'}
tie = {'A': 'X', 'B': 'Y', 'C': 'Z'}
lose = {'A': 'Z', 'B': 'X', 'C': 'Y'}
points = {'X': 1, 'Y': 2, 'Z': 3}

for i in lines:
    if i[1] == 'X': i[1]  = lose[i[0]]
    elif i[1] == 'Y': i[1] = i[1] = tie[i[0]]
    else: i[1] = win[i[0]]


total = 0
for i in lines:
    single = points[i[1]]
    if tie[i[0]] == i[1]: single += 3
    elif win[i[0]] == i[1]: single += 6
    total += single

print(total)