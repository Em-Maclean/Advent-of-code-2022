f = open("9.txt","r").readlines()

def nextto(h,t):
    #print(h,t)
    if h[0] == t[0]:
        if h[1] == t[1] or h[1] == t[1] + 1 or h[1] == t[1] - 1:
            return True

    if h[1] == t[1]:
        if h[0] == t[0] or h[0] == t[0] + 1 or h[0] == t[0] - 1:
            return True

    if h[0] == t[0] - 1 and h[1] == t[1] -1:
        return True
    
    if h[0] == t[0] - 1 and h[1] == t[1] +1:
        return True

    if h[0] == t[0] + 1 and h[1] == t[1] -1:
        return True

    if h[0] == t[0] + 1 and h[1] == t[1] +1:
        return True

    return False

def step(h,t,vals):

    while not nextto(h,t):

        if h[0] == t[0]:
            if h[1] > t[1]:
                t[1] += 1
            else:
                t[1] -= 1

        elif h[1] == t[1]:
            if h[0] > t[0]:
                t[0] += 1
            else:
                t[0] -= 1

        else:
            if h[0] > t[0] and h[1] > t[1]:
                t[0] += 1
                t[1] += 1

            elif h[0] > t[0] and h[1] < t[1]:
                t[0] += 1
                t[1] -= 1

            elif h[0] < t[0] and h[1] > t[1]:
                t[0] -= 1
                t[1] += 1

            else:
                t[0] -= 1
                t[1] -= 1

            
        n = str(t[0])+" " +str(t[1])
        if n not in vals:
            vals.append(n)

    return h,t,vals

def step_two(h,t):
    while not nextto(h,t):

        if h[0] == t[0]:
            if h[1] > t[1]:
                t[1] += 1
            else:
                t[1] -= 1

        elif h[1] == t[1]:
            if h[0] > t[0]:
                t[0] += 1
            else:
                t[0] -= 1

        else:
            if h[0] > t[0] and h[1] > t[1]:
                t[0] += 1
                t[1] += 1

            elif h[0] > t[0] and h[1] < t[1]:
                t[0] += 1
                t[1] -= 1

            elif h[0] < t[0] and h[1] > t[1]:
                t[0] -= 1
                t[1] += 1

            else:
                t[0] -= 1
                t[1] -= 1

    return t[0],t[1]

def partone(f,vals):


    #print(f)

    h = [0,0]
    t = [0,0]
    #vals.append(t)

    for i in range (len(f)):
        f[i] = f[i].split(" ")
        f[i][1] = f[i][1][:-1]

        if f[i][0] == "R":
            for k in range (int(f[i][1])):
                h[0] += 1
                h,t,vals = step(h,t,vals)

        elif f[i][0] == "L":
            for k in range (int(f[i][1])):
                h[0] -= 1
                h,t,vals = step(h,t,vals)


        elif f[i][0] == "U":
            for k in range (int(f[i][1])):
                h[1] += 1
                h,t,vals = step(h,t,vals)

        else:
            for k in range (int(f[i][1])):
                h[1] -= 1
                h,t,vals = step(h,t,vals)

            
    return len(vals)

def parttwo(f,vals):
   
    x = [0,0,0,0,0,0,0,0,0,0]
    y = [0,0,0,0,0,0,0,0,0,0]

    #vals.append(t)

    for i in range (len(f)):
        f[i] = f[i].split(" ")
        f[i][1] = f[i][1][:-1]

        if f[i][0] == "R":
            for k in range (int(f[i][1])):
                x[0] += 1
                for l in range (1,len(x)):
                    x[l], y[l] = step_two([x[l-1],y[l-1]],[x[l],y[l]])
                n = str(x[-1])+" " +str(y[-1])
                if n not in vals:
                    vals.append(n)

        elif f[i][0] == "L":
            for k in range (int(f[i][1])):
                x[0] -= 1
                for l in range (1,len(x)):
                    x[l], y[l] = step_two([x[l-1],y[l-1]],[x[l],y[l]])
                n = str(x[-1])+" " +str(y[-1])
                if n not in vals:
                    vals.append(n)


        elif f[i][0] == "U":
            for k in range (int(f[i][1])):
                y[0] += 1
                for l in range (1,len(x)):
                    x[l], y[l] = step_two([x[l-1],y[l-1]],[x[l],y[l]])
                n = str(x[-1])+" " +str(y[-1])
                if n not in vals:
                    vals.append(n)

        else:
            for k in range (int(f[i][1])):
                y[0] -= 1
                for l in range (1,len(x)):
                    x[l], y[l] = step_two([x[l-1],y[l-1]],[x[l],y[l]])

                n = str(x[-1])+" " +str(y[-1])
                if n not in vals:
                    vals.append(n)

        #print(x,y)
    
    return len(vals)
  
    
                

vals = ['0 0'] 
#print(partone(f,vals))
print(parttwo(f,vals))