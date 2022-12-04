
sacks = [ ]

with open("sample.txt") as f:
#with open("puzzle_input.txt") as f:

    for line in f.readlines():
        items = []
        for i in line.strip().split(' '):
            items.append(i)
        sacks.append(items)


data = "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"
x = len(data) 
compartment1 = slice(0,len(data)//2)
compartment2 = slice(len(data)//2, len(data))
print(data[compartment1], data[compartment2])