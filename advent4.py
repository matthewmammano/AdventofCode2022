txt = open('text4.txt', 'r')
lines = txt.readlines()
newLines = []
for i in lines:
    newLines += [i.split('\n')[0].split(',')]

lines = newLines

sum = 0
count = 0

# for i in lines:
#     print(i)
#     count += 1
#     a, b = i[0].split('-'), i[1].split('-')
#     a[0], b[0], a[1], b[1] = int(a[0]), int(b[0]), int(a[1]), int(b[1])
#     if (b[0] <= a[0] and b[1] >= a[1]) or (a[0] <= b[0] and a[1] >= b[1]): 
#         sum += 1
# print(sum)

for i in lines:
    print(i)
    count += 1
    a, b = i[0].split('-'), i[1].split('-')
    a[0], b[0], a[1], b[1] = int(a[0]), int(b[0]), int(a[1]), int(b[1])
    if (b[0] >= a[0] and b[0] <= a[1]) or (a[0] >= b[0] and a[0] <= b[1]) or (b[1] <= a[1] and b[1] >= a[0]) or (a[1] <= b[1] and a[1] >= b[0]): 
        sum += 1
print(sum)