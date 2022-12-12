import math

f = open("11.txt","r").readlines()

monkeys = []

for i in range (0,len(f),7):
    new_monkey = []
    new_monkey.append(len(monkeys))
    f[i+2] = f[i+2][:-1].split(" ")
    new_monkey.append(f[i+2][5])
    new_monkey.append(f[i+2][6])
    new_monkey.append(f[i+2][7])
    f[i+3] = f[i+3][:-1].split(" ")
    new_monkey.append(f[i+3][5])
    f[i+4] = f[i+4][:-1].split(" ")
    f[i+5] = f[i+5][:-1].split(" ")
    new_monkey.append(f[i+4][-1])
    new_monkey.append(f[i+5][-1])
    f[i+1] = f[i+1].split(" ")
    for n in range (4,len(f[i+1])):
        new_monkey.append(f[i+1][n][:-1])

    monkeys.append(new_monkey)


counter = []
for n in monkeys:
    counter.append(0)

for m in range (10000):
    for i in range (len(monkeys)):
        n = 7
        while len(monkeys[i]) > 7:
            
            if monkeys[i][2] == "*":
                if monkeys[i][3] == "old":
                    monkeys[i][n] = int(monkeys[i][n]) * int(monkeys[i][n])
                else:
                    monkeys[i][n] = int(monkeys[i][n]) * int(monkeys[i][3])
            else:
                monkeys[i][n] = int(monkeys[i][n]) + int(monkeys[i][3])

            counter[int(monkeys[i][0])] += 1

            #monkeys[i][n] = math.floor(int(monkeys[i][n]) / 3)
            monkeys[i][n] = int(monkeys[i][n]) % 9699690
            #(n mod p) mod d = n mod d

            if monkeys[i][n] % int(monkeys[i][4]) == 0:
                #print(int(monkeys[i][5]))
                #print(monkeys[i])
                monkeys[int(monkeys[i][5])].append(monkeys[i][n])
            else:
                monkeys[int(monkeys[i][6])].append(monkeys[i][n])

            del monkeys[i][n]


counter = sorted(counter)
print(counter[-1] * counter[-2])