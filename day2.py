#Advent of Code - Day 2

#Part 1

infile = open("day2input.txt","r")
li = infile.read()
li = li.split("\n")

twice = 0
trice = 0

def check(idk):
    
    di = 0
    tri = 0
    chars = list()
    
    for x in range(len(idk)):
        if idk[x] not in chars:
            tmp = idk.count(idk[x])
            chars.append(idk[x])
            if tmp is 2:
                di += 1
            elif tmp is 3:
                tri += 1
            tmp = 0
    
    card = [di, tri]
    return card

for i in range(len(li)):
    res = check(li[i])
    twice += res[0]
    trice += res[1]

print ("Part 1: ", twice * trice) #checksum