#importing ascii_letters
from string import ascii_letters

# Reading in puzzle data
#with open("sample.txt") as f:
with open("puzzle_input.txt") as f:
    #Nesting data input prep into the list.
    sacks = [ line for line in f.read().strip().split("\n")]

#Variable to track "total score" of all the sacks
total = 0

# Loop through the data and determine the half way point of each string.
for i in sacks:
    split = len(i)//2
    #Split the sack into two compartments
    compartment1 = set(i[:split])
    compartment2 = set(i[split:])
    # Loop through the data and assign the char a number value, compare compartments and add the number
    # and 1, because the dataset starts at 0.
    for priority, char in enumerate(ascii_letters):
        if char in compartment1 and char in compartment2:
            total += priority + 1
print(total)

# Part 2

#Loop through the data using 3 elements at a time.
teamtotal = 0 
teamsize = 3
for i in range(0, len(sacks),3):
    teams = sacks[i:teamsize]
    teamsize += 3
    #print(teams)

# Same as above, except comparing 3 rucksacks at a time.
    for priority, char in enumerate(ascii_letters):
        if char in teams[0] and char in teams[1] and char in teams[2]:
            teamtotal += priority + 1
print(teamtotal)