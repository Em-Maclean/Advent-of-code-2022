f = open("2.txt","r").readlines()

score = 0
score2 = 0

for i in range (len(f)):
    hand = f[i][:-1].split(" ")

    if hand[0] == "A":
        if hand[1] == "X":
            score += 4
            score2 += 3
        elif hand[1] == "Y":
            score += 8
            score2 += 4
        else:
            score += 3
            score2 += 8
    elif hand[0] == "B":
        if hand[1] == "X":
            score += 1
            score2 += 1
        elif hand[1] == "Y":
            score += 5
            score2 += 5
        else:
            score += 9
            score2 += 9
    else:
        if hand[1] == "X":
            score += 7
            score2 += 2
        elif hand[1] == "Y":
            score += 2
            score2 += 6
        else:
            score += 6
            score2 += 7

print(score)
print(score2)