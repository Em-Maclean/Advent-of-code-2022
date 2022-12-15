import math
import json
'''
f = [[1,1,3,1,1],
    [1,1,5,1,1],
    [[1],[2,3,4]],
    [[1],4],
    [9],
    [[8,7,6]],
    [[4,4],4,4],
    [[4,4],4,4,4],
    [7,7,7,7],
    [7,7,7],
    [],
    [3],
    [[[]]],
    [[]],
    [1,[2,[3,[4,[5,6,7]]]],8,9],
    [1,[2,[3,[4,[5,6,0]]]],8,9]]
'''
def check(a, b):
    if str(a).isnumeric() and str(b).isnumeric():
        if a == b:
            return "keep checking"
        elif a > b:
            return "wrong"
        else:
            return "right"

    else:
        if str(a).isnumeric():
            a = [a]
        elif str(b).isnumeric():
            b = [b]

        if len(a) < len(b):
            for k in range (len(a)):
                if not str(a[k]).isnumeric() or not str(b[k]).isnumeric():
                    val = check(a[k],b[k])
                    if val != "keep checking":
                        return val
                elif a[k] < b[k]:
                    return "right"
                elif a[k] > b[k]:
                    return "wrong"
            return "right"

        elif len(b) < len(a):
            for k in range (len(b)):
                if not str(a[k]).isnumeric() or not str(b[k]).isnumeric():
                    val = check(a[k],b[k])
                    if val != "keep checking":
                        return val
                elif a[k] < b[k]:
                    return "right"
                elif a[k] > b[k]:
                    return "wrong"
            return "wrong"
        
        else:
            for k in range (len(a)):
                if not str(a[k]).isnumeric() or not str(b[k]).isnumeric():
                    val = check(a[k],b[k])
                    if val != "keep checking":
                        return val
                elif a[k] < b[k]:
                    return "right"
                elif a[k] > b[k]:
                    return "wrong"
            return "keep checking"


f = open("13.txt").readlines()
for i in range (0,len(f),3):
    f[i] = (json.loads(f[i][:-1]))
    f[i+1] = (json.loads(f[i+1][:-1]))


ans = []
for i in range (0,len(f),3):
    if len(ans) == 0:
        one = f[i]
        two = f[i+1]

        count = 0
        m = min([len(one),len(two)])
        message = "keep checking"

        while message == "keep checking" and count < m:
            message = check(one[count], two[count])
            count += 1

        if message == "keep checking":
            if len(one) > len(two):
                message = "wrong"
            else:
                message = "right"

        if message == "right":
            ans.append(one)
            ans.append(two)
        else:
            ans.append(two)
            ans.append(one)
    else:
        j = [f[i],f[i+1]]
        for one in j:
            counter = 0
            message = "keep checking"
            while message != "right" and counter < len(ans):
                two = ans[counter]

                count = 0
                m = min([len(one),len(two)])
                message = "keep checking"

                while message == "keep checking" and count < m:
                    message = check(one[count], two[count])
                    count += 1

                if message == "keep checking":
                    if len(one) > len(two):
                        message = "wrong"
                    else:
                        message = "right"

                if message == "right":
                    ans.insert(counter,one)

                counter += 1
            
            if message == "wrong":
                ans.append(one)
            
nums = []
for n in range (len(ans)):
    if ans[n] == [[2]] or ans[n] == [[6]]:
        nums.append(n+1)

print(nums[0]*nums[1])
