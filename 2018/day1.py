#Advent of Code - Day 1

infile = open("day1input.txt", "r")
inputlist = infile.read()
inputlist = inputlist.split("\n") #converts string to list

#Part 1

current_sum = 0
for x in inputlist:        
    current_sum += int(x)

print("Part 1: ", current_sum) #525

#Part 2

current_sum = 0
flag = True
used = set()   #list of all used frequencys
used.add(current_sum)

while(flag):
    for x in inputlist:
        current_sum += int(x)
        if current_sum in used:
            flag = False
            break
        else:
            used.add(current_sum)

print("Part 2: ", current_sum) #75749