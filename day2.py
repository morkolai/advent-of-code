#Advent of Code - Day 2

infile = open("day2input.txt","r")
li = infile.read()
li = li.split("\n")

#Part 1:

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

#Part 2:

def idpair(idone, idtwo):

    letter = -1

    for x in range(len(idone)):

        if idone[x] != idtwo[x]:
            if letter == -1:
                letter = x
            else:
                return -1
    return letter

diff = 0

for i in range(len(li)):
    for j in range(i+1, len(li)):
        if idpair(li[i],li[j]) != -1:
            idcode = li[i]
            diff = idpair(li[i],li[j])
            break
    if diff:
        break

print("Part 2: ", idcode[0:diff],idcode[diff+1:len(idcode)]) #n mgyjkpruszlbaqwficavxneo