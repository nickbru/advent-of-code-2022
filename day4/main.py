# Read in data and format it.
#with open("sample.txt") as f:
with open("puzzle_input.txt") as f: 
	data = f.read().strip().split()

#Define variable to track answer.
total = 0
# Defining variable for part 2
p2total = 0

# Loop through the data and split it into elves by the "," Then define the ranges of each elf in a list by the -. Mapping the data to ints.
for i in data:
	elves = i.split(",")
	ranges = [list(map(int, elf.split("-"))) for elf in elves]

# Define the Elf 1 & 2 start area and end area.
	E1as, E1ae = ranges[0]
	E2as, E2ae = ranges[1]

	if E1as <= E2as and E1ae >= E2ae or E1as >= E2as and E1ae <= E2ae:
		total += 1

# Part 2
# Need to determine if the elves ranges overlap at all. Accomplished by comparing if Elf 1 end is less than Elf 2 start
# and if Elf 2 area end is less than Elf 1 area start. All other cases overlap so incirment the answer by 1.

	if not (E1ae < E2as or E2ae < E1as):
		p2total += 1

# Print the Answers.
print(total)
print(p2total)