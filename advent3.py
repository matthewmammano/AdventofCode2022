def getPoints(str):
    num = ord(str)
    if num > 90: return num - 70
    else: return num - 64

def shared(str):
    s1, s2 = str[:len(str)//2], str[len(str)//2:]
    for i in s1:
        for j in s2:
            if i == j: return getPoints(i)
    raise ValueError("Date provided can't be in the past")

def shared3(ls):
    for i in ls[0]:
        for j in ls[1]:
            for k in ls[2]:
                if i == j and i == k: return getPoints(i.swapcase())


# txt = open('text3.txt', 'r')
# lines = txt.readlines()
# lines = list(map(lambda i: i[:-1], lines))
# lines = list(map(lambda i: i.swapcase(), lines))

# sum = 0
# for i in lines:
#     sum += shared(i)
# print(sum)

txt = open('text3b.txt', 'r')
lines = txt.readlines()
lines = list(map(lambda i: i[:-1], lines))

newLines = []
for i in range(0, len(lines), 3):
    newLines += [[lines[i]] + [lines[i + 1]] + [lines[i + 2]]]

sum = 0
for i in newLines:
    sum += shared3(i)
print(sum)