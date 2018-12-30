#Advent of Code - Day 2

#Part 1

infile = open("day2input.txt","r")
li = infile.read()
li = li.split("\n")

twice = 0
trice = 0

def check(boxid):
    
    di = False
    tri = False
    chars = list()
    
    for x in range(len(boxid)):
        if boxid[x] not in chars:
            num = boxid.count(boxid[x])
            chars.append(boxid[x])
            if num == 2 and di == False:
                di = True
            elif num == 3 and tri == False:
                tri = True

    card = [di, tri]
    return card

for i in range(len(li)):
    res = check(li[i])
    twice += int(res[0])
    trice += int(res[1])


print ("Part 1: ", twice * trice) #checksum = 5658