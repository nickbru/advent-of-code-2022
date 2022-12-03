# Createing an empty list to store the encrypted game data
# Reading in each line striping whitespace and spliting by spaces adding this to a new list called games
# All of this data is added back to the encrypted list

encrypted = [ ]

#Two open commands to read in the sample/final inputs
#with open("sample.txt") as f:
with open("puzzle_input.txt") as f:
    for line in f.readlines():
        games = []
        for rps in line.strip().split(' '):
            games.append(rps)
        encrypted.append(games)

# Printing out the data to confirm its a list of lists        
#print(encrypted),print(type(encrypted))

# Setting a variable to track the RPS scores
total = 0

# ROCK:A,X  PAPER:B,Y SCISSORS:C,Z
# Allocate points to total for "my" moves
for RPS in encrypted:
    if RPS[1] == 'X':
        total += 1
    elif RPS[1] == 'Y':
        total += 2
    elif RPS[1] == 'Z':
        total += 3

# Determine Win and Tie outcomes and allocate points 
    if RPS[0] == 'B' and RPS[1] =='Z':
        total += 6
    elif RPS[0] == 'A' and RPS[1] =='Y':
        total += 6
    elif RPS[0] == 'C' and RPS[1] =='X':
        total += 6
    elif RPS[0] == 'A' and RPS[1] =='X':
        total += 3
    elif RPS[0] == 'B' and RPS[1] =='Y':
        total += 3
    elif RPS[0] == 'C' and RPS[1] =='Z':
        total += 3

# print total variable of all the games.
print(total)

# Part II 
#X:Loose Y:Tie Z:Win
# 1 for Rock, 2 for Paper, and 3 for Scissors

# Setting a varaible for tracking new total
p2total = 0

# Allocate points for ties and wins
for RPS2 in encrypted:
    if RPS2[1] == "Y":
        p2total += 3
    if RPS2[1] == "Z":
        p2total += 6

# Itterate scoring for possible outcomes for wins,ties,losses to determine points for "my" play.
    if RPS2[0] == 'A' and RPS2[1] =='X':
        p2total += 3
    elif RPS2[0] == 'A' and RPS2[1] =='Y':
        p2total += 1
    elif RPS2[0] == 'A' and RPS2[1] =='Z':
        p2total += 2
    elif RPS2[0] == 'B' and RPS2[1] =='X':
        p2total += 1
    elif RPS2[0] == 'B' and RPS2[1] =='Y':
        p2total += 2
    elif RPS2[0] == 'B' and RPS2[1] =='Z':
        p2total += 3
    elif RPS2[0] == 'C' and RPS2[1] =='X':
        p2total += 2
    elif RPS2[0] == 'C' and RPS2[1] =='Y':
        p2total += 3
    elif RPS2[0] == 'C' and RPS2[1] =='Z':
        p2total += 1

# Print the total for part2
print(p2total)