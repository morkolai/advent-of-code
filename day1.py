#Advent of Code - Day 1
#Part 1

infile = open("day1input.txt", "r")
inputlist = infile.read()
inputlist = inputlist.split("\n") #converts string to list

sum = 0
for x in inputlist:        
    sum += int(x)

print("Part 1: ", sum) #525

#Part 2

sum = 0
flag = True
used = list()   #list of all used frequencys
used.append(sum)

while(flag):
   for x in inputlist:
       sum += int(x)
       if sum in used:
           flag = False
           break
       used.append(sum)

print("Part 2: ", sum) #75749