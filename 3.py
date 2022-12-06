f = open("3.txt","r").readlines()

both = []
'''
for i in range (len(f)):
    f[i] = f[i][:-1]
    one = f[i][:int(len(f[i])/2)]
    two = f[i][int(len(f[i])/2):]

    this_both = []
    for x in one:
        if x in two and x not in this_both:
            this_both.append(x)

    both = both + this_both
'''

for i in range(0,len(f),3):
    one = f[i][:-1]
    two = f[1+i][:-1]
    three = f[i+2][:-1]
    this_both = []

    for x in one:
        if x in two and x in three and x not in this_both:
            this_both.append(x)

    both = both + this_both


count = 0

for x in both:
    if x.upper() == x:
        count += ord(x) - 38
        #print(ord(x) - 38)
    else:
        count += ord(x) - 96
        #print(ord(x) - 96)

print(count)


