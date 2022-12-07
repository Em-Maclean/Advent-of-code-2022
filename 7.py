f = open("7.txt","r").readlines()

    

def partone(f):

    current_nodes = []
    sizes = []

    for i in range (len(f)):
        f[i] = f[i][:-1].split(" ")

        if f[i][0] == "$":

            if f[i][1] == "cd":

                if f[i][2] != "..":
                    current_nodes.append(0)
                else:
                     sizes.append(current_nodes[-1])
                     del current_nodes[-1]   

        elif f[i][0] != "dir":
            for n in range(len(current_nodes)):
                current_nodes[n] += int(f[i][0])

    for n in current_nodes:
        sizes.append(n)

    ans = 0
    for n in sizes:
        if n <= 100000:
            ans += n

    return ans

def parttwo(f):
    current_nodes = []
    sizes = []

    for i in range (len(f)):
        f[i] = f[i][:-1].split(" ")

        if f[i][0] == "$":

            if f[i][1] == "cd":

                if f[i][2] != "..":
                    current_nodes.append(0)
                else:
                     sizes.append(current_nodes[-1])
                     del current_nodes[-1]   

        elif f[i][0] != "dir":
            for n in range(len(current_nodes)):
                current_nodes[n] += int(f[i][0])

    for n in current_nodes:
        sizes.append(n)

    UNUSED = 70000000 - max(sizes)
    SPACE_NEEDED = 30000000

    pos = []
    for n in sizes:
        if UNUSED + n > SPACE_NEEDED:
            pos.append(n)

    return min(pos)


#print(partone(f))
print(parttwo(f))
