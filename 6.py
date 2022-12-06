f = open("6.txt","r").readlines()
f = list(f[0])

def partone(f):

    count = 0
    found = False

    while not found:

        found = True

        l = [f[count], f[count+1], f[count+2], f[count+3]]
        l = sorted(l)
        for i in range (len(l)-1):
            if l[i] == l[i+1]:
                found = False

        count += 1
    
    return count + 3

def parttwo(f):

    count = 0
    found = False

    while not found:

        found = True

        l = []
        for i in range (14):
            l.append(f[count+i])

        l = sorted(l)
        for i in range (len(l)-1):
            if l[i] == l[i+1]:
                found = False

        count += 1
    
    return count + 13


print(partone(f))
print(parttwo(f))