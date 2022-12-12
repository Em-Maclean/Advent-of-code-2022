f = open("8.txt","r").readlines()


def partone(f):

    seen = []
    for i in range (len(f)):
        line = []
        for j in range(len(f[i])):
            line.append(".")
        seen.append(line)

    count = 0

    for i in range (len(f[0])):
        max_val = -1
        for j in range (len(f)):
            if int(f[j][i]) > max_val and seen[j][i] != "s":
                count += 1
                seen[j][i] = "s"
                max_val = int(f[j][i])
            elif int(f[j][i]) > max_val:
                max_val = int(f[j][i])
            

    #print(count)

    for i in range (len(f[-1])):
        max_val = -1
        for j in range (len(f)-1,-1,-1):
            if int(f[j][i]) > max_val and seen[j][i] != "s":
                count += 1
                seen[j][i] = "s"
                max_val = int(f[j][i])
            elif int(f[j][i]) > max_val:
                max_val = int(f[j][i])

    #print(count)

    for i in range(1,len(f)-1):
        
        max_val = -1
        for j in range (len(f[i])):
            if int(f[i][j]) > max_val and seen[i][j] != "s":
                count += 1
                seen[i][j] = "s"
                max_val = int(f[i][j])
            elif int(f[i][j]) > max_val:
                max_val = int(f[i][j])


        max_val = -1
        for j in range (len(f[i])-1,-1,-1):
            if int(f[i][j]) > max_val and seen[i][j] != "s":
                count += 1
                seen[i][j] = "s"
                max_val = int(f[i][j])
            elif int(f[i][j]) > max_val:
                max_val = int(f[i][j])

    return count

def parttwo(f):

    max_val = 0

    for i in range (1,len(f)-1):
        for j in range (1,len(f[i])-1):
            #up
            up_score = 0
            y_count = i - 1
            while y_count >= 0 and int(f[i][j]) > int(f[y_count][j]):
                up_score += 1
                y_count -= 1

            if y_count >= 0:
                up_score += 1

            #down
            down_score = 0
            y_count = i + 1
            while y_count < len(f) and int(f[i][j]) > int(f[y_count][j]):
                down_score += 1
                y_count += 1

            if y_count < len(f):
                down_score += 1

            #left
            left_score = 0
            x_count = j - 1
            while x_count >= 0 and int(f[i][j]) > int(f[i][x_count]):
                left_score += 1
                x_count -= 1
            
            if x_count >= 0:
                left_score += 1

            #right
            right_score = 0
            x_count = j + 1
            while x_count < len(f[i]) and int(f[i][j]) > int(f[i][x_count]):
                right_score += 1
                x_count += 1

            if x_count < len(f[i]):
                right_score += 1
        
            score = up_score * down_score * left_score * right_score
            #print(up_score, down_score, left_score, right_score)
            if score > max_val:
                max_val = score

    return max_val


for i in range(len(f)):
    f[i] = list(f[i][:-1])

#print(partone(f))
print(parttwo(f))