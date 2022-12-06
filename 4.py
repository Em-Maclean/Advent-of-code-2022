f = open("4.txt","r").readlines()

for i in range (len(f)):
    f[i] = f[i][:-1].split(",")
    f[i][0] = f[i][0].split("-")
    f[i][1] = f[i][1].split("-")
    f[i][0][0] = int(f[i][0][0])
    f[i][0][1] = int(f[i][0][1])
    f[i][1][0] = int(f[i][1][0])
    f[i][1][1] = int(f[i][1][1])

def partone(f):

    count = 0

    for i in range (0,len(f)):

        if f[i][0][1] - f[i][0][0] > f[i][1][1] - f[i][1][0]:
            if f[i][1][1] <= f[i][0][1] and f[i][1][0] >= f[i][0][0]:
                count += 1
        elif f[i][0][1] - f[i][0][0] < f[i][1][1] - f[i][1][0]:
            if f[i][0][1] <= f[i][1][1] and f[i][0][0] >= f[i][1][0]:
                count += 1
        else:
            if f[i][0] == f[i][1]:
                count += 1
    
    return count


def parttwo(f):

    count = 0

    for line in f:
        if line[0][0] <= line[1][0] and line[0][1] >= line[1][0]:
            count += 1
        elif line[1][0] <= line[0][0] and line[1][1] >= line[0][0]:
            count += 1
        elif line[0][0] >= line[1][0] and line[0][0] <= line[1][1]:
            count += 1
        elif line[1][0] >= line[0][0] and line[1][0] <= line[0][1]:
            count += 1

    return count


print(partone(f))
print(parttwo(f))

