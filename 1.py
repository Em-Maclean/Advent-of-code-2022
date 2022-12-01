f = open("1.txt","r").readlines()

count = 0
cal = []

for i in range (len(f)):
    f[i] = f[i][:-1]

    if f[i] == "":
        cal.append(count)
        count = 0
    else:
        count += int(f[i])

cal = sorted(cal)
print(max(cal))
print(cal[-1] + cal[-2] + cal[-3])