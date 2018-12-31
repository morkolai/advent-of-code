#Advent of Code - Day 3

#Part 1:

infile = open("day3input.txt","r")
tmpli = infile.read()
tmpli = tmpli.split("\n")
li = list()

#Creates a handy list of the inputfile

for x in range(len(tmpli)):
    claim =  tmpli[x]
    ID = int(claim[1:claim.find(" ")])
    left = int(claim[claim.find("@")+2:claim.find(",")])
    top = int(claim[claim.find(",")+1:claim.find(":")])
    width = int(claim[claim.find(":")+2:claim.find("x")])
    length = int(claim[claim.find("x")+1:len(claim)])
    li.append([ID, left, top, width, length])

print(li[1][1])