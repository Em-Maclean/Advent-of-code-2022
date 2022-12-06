b = open("5.txt","r").readlines()

def partone(f):

    stack = True
    stacks = []

    for i in range(len(f)):
        if i == 0:
            for n in range (9):
                stacks.append([])
        
        keep = f[i].split(" ")
        f[i] = list(f[i][:-1])
        
        if len(f[i]) == 0 or f[i][1] == "1" or f[i] == "":
            stack = False

        elif stack:
            count = 0
            for n in range (1,len(f[i]),4):
                if f[i][n] != ' ':
                    stacks[count].insert(0,f[i][n])
                count += 1

            #print(stacks)

        else:
            nums = [keep[1],keep[3],keep[5][:-1]]
            val = stacks[int(nums[1])-1][len(stacks[int(nums[1])-1])-int(nums[0]):]
            stacks[int(nums[1])-1] = stacks[int(nums[1])-1][:len(stacks[int(nums[1])-1])-len(val)]
            for n in range (len(val)-1,-1,-1):
                stacks[int(nums[2])-1].append(val[n])


    ans = ""
    for n in stacks:
        ans += n[-1]

    return ans

def parttwo(f):

    stack = True
    stacks = []

    for i in range(len(f)):
        if i == 0:
            for n in range (9):
                stacks.append([])
        
        keep = f[i].split(" ")
        f[i] = list(f[i][:-1])
        
        if len(f[i]) == 0 or f[i][1] == "1" or f[i] == "":
            stack = False

        elif stack:
            count = 0
            for n in range (1,len(f[i]),4):
                if f[i][n] != ' ':
                    stacks[count].insert(0,f[i][n])
                count += 1

            #print(stacks)

        else:
            nums = [keep[1],keep[3],keep[5][:-1]]
            val = stacks[int(nums[1])-1][len(stacks[int(nums[1])-1])-int(nums[0]):]
            stacks[int(nums[1])-1] = stacks[int(nums[1])-1][:len(stacks[int(nums[1])-1])-len(val)]
            for n in range (len(val)):
                stacks[int(nums[2])-1].append(val[n])


    ans = ""
    for n in stacks:
        ans += n[-1]

    return ans

#print(partone(b))
print(parttwo(b))

