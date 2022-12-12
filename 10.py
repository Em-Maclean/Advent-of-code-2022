f = open("10.txt","r").readlines()

def partone(f):
    l = [20,60,100,140,180,220]
    cycle = 0
    count = 1
    counter = []

    for i in range (len(f)):
        f[i] = f[i][:-1].split(" ")

        if f[i][0] == "addx":
            cycle += 1
            if cycle in l:
                counter.append(cycle*count)
                #print(cycle, count, cycle*count,i)
            cycle += 1
            if cycle in l:
                counter.append(cycle*count)
                #print(cycle, count, cycle*count,i)
            count += int(f[i][1])
        else:
            cycle += 1
            if cycle in l:
                counter.append(cycle*count)
                #print(cycle, count, cycle*count,i)
        
       

    c = 0
    for i in counter:
        c += i

    return c

def parttwo(f):
    
    count = 1
    counter = ["","","","","",""]
    
    point = 0

    for i in range (len(f)):
        f[i] = f[i][:-1].split(" ")

        if f[i][0] == "addx":
             
            if count == len(counter[point]) or count + 1 == len(counter[point]) or count - 1 == len(counter[point]):
                counter[point] += "#"

                if len(counter[point]) == 40:
                    point += 1
                    
            else:
                counter[point] += "."
            
                if len(counter[point]) == 40:
                    point += 1
                    

            if count == len(counter[point]) or count + 1 == len(counter[point]) or count - 1 == len(counter[point]):
                counter[point] += "#"
                
                if len(counter[point]) == 40:
                    point += 1
                    
            else:
                counter[point] += "."
    
                if len(counter[point]) == 40:
                    point += 1
                    
            count += int(f[i][1])

        else:
            
            if count == len(counter[point]) or count + 1 == len(counter[point]) or count - 1 == len(counter[point]):
                counter[point] += "#"
    
                if len(counter[point]) == 40:
                    point += 1
                    
            else:
                counter[point] += "."
            
                if len(counter[point]) == 40:
                    point += 1    
                
    for n in counter:
        print(n)

#print(partone(f))
parttwo(f)
