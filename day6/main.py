#Opening the input data, reading it in as data.
with open("puzzle_input.txt") as f: 
    data = f.read().strip()

#adding variables for p1,p2 solutions.
#part = 4
part = 14

#print(data)

#Loop through the length of data 4 characters at a time. Store this input as "marker", remove any duplicate elements using set.
for i in range(part, len(data)):
    marker = set(data[(i-part):i])
# Check to see if marker is 4 elements in length if so print it's index value.
    if len(marker) == part:
        print(i)
        break #Neat

#Part two is looking for messages of 14 char length of non repeating charaters. Changed the range from 4 to 14.
