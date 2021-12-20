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

#Creates a matrix representation of the fabric claims

matrix = list()
maxWidth = 0
maxHeigth = 0

    #Finds width and heigth

for x in range(len(tmpli)):
    if (li[x][1] + li[x][3]) > maxWidth:
        maxWidth = li[x][1] + li[x][3]
    if (li[x][2]) + (li[x][4]) > maxHeigth:
        maxHeigth = li[x][2] + li[x][4]

    #Fills the matrix with zeros

for x in range(maxWidth):
    row = list()
    for y in range(maxHeigth):
        row.append(0)
    matrix.append(row)

#Marks all the claims with +1

def markClaim(claim):
    xpos = claim[1]
    ypos = claim[2]
    for i in range(claim[3]):
        for j in range(claim[4]):
            matrix[i][j] += 1
            print(matrix[i][j])

for x in range(len(li)):
    markClaim(li[x])

#Counts overlapping square inches

squareInches = 0

for x in range(maxWidth):
    for y in range(maxHeigth):
        if matrix[x][y] > 1:
            squareInches += 1

#Prints result (Currently 841)

print("Part 1: ", squareInches)