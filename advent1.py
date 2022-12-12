myfile = open("text1.txt", "r")
contents = myfile.read()
myfile.close()

contents = contents.split("\n\n")

max1 = 0
max2 = 0
max3 = 0
for i in contents:
    count = 0
    for j in i.split("\n"):
        count += int(j)
    if count > max1: max1,max2,max3 = count,max1,max2
    elif count > max2: max2,max3 = count, max2
    elif count > max3: max3 = count
