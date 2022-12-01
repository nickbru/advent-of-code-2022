#f = open("sample.txt").read()
f = open("puzzle_input.txt").read()

total_list = [ ]

#strip whitespace, and split data by new lines
for elf in f.strip().split("\n\n"):
    #print(elf)
#Add up each chunk of data
    total_list.append(sum(int(cal) for cal in elf.split("\n")))
    #print(type(max(totalc))),print(totalc)

#Print the highest total
#print(total_list)
print(max(total_list))

#Print the highest three totals
print(f"{sum(sorted(total_list, reverse=True)[:3])}")