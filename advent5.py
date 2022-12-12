txt = open('text5.txt', 'r')
lines = txt.read()
lines = lines.split('\n\n')

width = len(lines[0].split('\n')[0])

storage = []
for i in range(0, width, 4):
    temp = []
    for j in range(len(lines[0].split('\n'))):
        temp += [lines[0].split('\n')[j][i : i+3]]
    storage += [temp]

dict = {}
for i in storage:
    dict[int(i[-1])] = i[:-1]

for i in dict.keys():
    element = dict[i]
    newElement = []
    for j in element:
        if j != '   ':
            newElement += [j]
    dict[i] = newElement

instructions = lines[1].split('\n')
newInst = []
for i in instructions:
    newInst += [i.split(' ')[1::2]]
instructions = newInst

newInstr = []
for i in instructions:
    newnewInstr = []
    for j in i:
        newnewInstr += [int(j)]
    newInstr += [newnewInstr]

instructions = newInstr

for i in instructions:
    repeat = i[0]
    take = dict[i[1]][:repeat]
    dict[i[1]] = dict[i[1]][repeat:]
    dict[i[2]] = take[::1] + dict[i[2]]

for i in dict.keys():
    print(dict[i][0])