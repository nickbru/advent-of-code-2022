#Read in the puzzle data and read each row.
with open ('puzzle_input.txt') as f:
    data = [row.strip() for row in f.readlines()]

#Determine the number of rows by determining the length of data and then the number of colums by reading the first element in all rows
ROWS = len(data)
COLUMNS = len(data[0])

# Determine the visible edges first and last row, and each colum, subtracting 2 so the corners are only counted once
edges = (ROWS * 2 ) + ((COLUMNS - 2) * 2)
total = edges

#Creating empty list to track part2 score
scores=[]

#Read through each tree that isn't an edge starting at first index skipping the last row and last colum
for row in range (1, ROWS - 1):
    for colum in range(1, COLUMNS -1):
        tree = data[row][colum]

        # Get all Trees to the left, right,top, bottom of current tree
        left = [data[row][colum - i] for i in range(1, colum +1)]
        right = [data[row][colum + i] for i in range(1, COLUMNS - colum)]
        up = [data[row - i][colum] for i in range(1, row +1)]
        down = [data[row + i][colum] for i in range(1, ROWS - row)]

        #part1
        #Using max to determine if interior trees are smaller than our selected tree.
        if max(left)<tree or max(right)<tree or max(up)<tree or max(down)<tree:
            total += 1

        #part2
        #Iterate through each direction of trees 
        totalp2 = 1 #Doesn't work when you set it to zero and multiply....
        for lst in (left,right,up,down):
            value = 0
            for i in range(len(lst)):
                if lst[i] < tree:
                    value += 1
                elif lst[i] >= tree:
                    value += 1
                    break
                else:
                    break

            totalp2 *= value
        #Add each value total to the score list.
        scores.append(totalp2)


        

print(total)
print(max(scores))

