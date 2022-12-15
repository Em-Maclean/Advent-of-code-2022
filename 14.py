f = open("14.txt","r").readlines()

grid = []
for i in range(300):
    line = []
    for k in range (1000):
        line.append(".")
    grid.append(line)

max_left = 100000000000
max_right = 0
max_down = 0

for i in range (len(f)):
    f[i] = f[i][:-1].split(" ")
    for k in range (0,len(f[i])-2,2):
        one = f[i][k].split(",")
        two = f[i][k+2].split(",")

        if one[0] == two[0]:
            start = min([int(one[1]),int(two[1])]) 
            end = max([int(one[1]),int(two[1])])

            if end > max_down:
                max_down = end

            while start <= end:
                grid[start][int(one[0])] = "#"
                start += 1
        else:
            start = min([int(one[0]),int(two[0])]) 
            end = max([int(one[0]),int(two[0])])

            if start < max_left:
                max_left = start
            if end > max_right:
                max_right = end

            while start <= end:
                grid[int(one[1])][start] = "#"
                start += 1

for i in range (len(grid[max_down+2])):
    grid[max_down+2][i] = "#"


start = [0,500]
abyss = False
count = 0
#print(max_left,max_right)


for b in range (100000):#while not abyss:
    co = [start[0],start[1]]
    while grid[co[0]+1][co[1]] == "." or grid[co[0]+1][co[1]-1] == "." or grid[co[0]+1][co[1]+1] == ".":
        if grid[co[0]+1][co[1]] == ".":
            co[0] += 1

        elif grid[co[0]+1][co[1]-1] == ".":
            co[0] += 1
            co[1] -= 1
            
        
        elif grid[co[0]+1][co[1]+1] == ".":
            co[0] += 1
            co[1] += 1

        #print(co)
            
         
    grid[co[0]][co[1]] = "o"
    if grid[0][500] == "o":
        print(count, "done")
        break
    count += 1
    #print(count)

print(count+1)

#for n in grid:
 #   print(n[max_left-1:max_right])

