with open("puzzle_input.txt") as f:
    #Create a dictionary
    directory = {} 
    #Create an emptylist 
    pwd = [] 
    #Read lines from input file
    lines = f.readlines()
    for line in lines:
        #Strip whitespace and splite lines
        commands = line.rstrip().split()
        #Determine if it is a command
        if commands[0] == "$":
            #Determine if it lists a directory
            if commands[1] == "ls":
                continue
            #Otherwise determine if it changes directory
            elif commands[1] == "cd":
                # Determine if your moving back up a folder
                if commands[2] == "..":
                    pwd = pwd[:-1]
                #Otherwise determine if moving back to /
                elif commands[2] == "/":
                    pwd = ["/"]
                #Append the data to the pwd list
                else:
                    pwd.append(commands[2])
        else:
            #If not commands id no] equal to dir
            if commands[0] != "dir":
                current_path = ""
                # for each folder in pwd determine if path is not equal to / and current path isn't /
                for folder in pwd:
                    if folder != "/" and current_path != "/":
                        #Add the value onto current path
                        current_path += "/"
                    current_path += folder
                    #Create entry in dictironary
                    directory[current_path] = directory.get(current_path,0) + int(commands[0])

#Define total variable and set to zero
total = 0
# Loop through the directory dictionary determine if the item is less than 100000 if so add to total
for item in directory.items():
    if item[1] < 100000:
        total += item[1]
#print total
print(total)

# define required space for update (subtract the total space - directorys in dic
required_space = 30000000 - (70000000 - directory.get("/"))
# Define the item to delete a infinite float
delete_item = float('inf')
#Loop through each item in the directory dictionary if the size of the item is greater or = to the required space
for item in directory.items():
    if item[1] >= required_space:
        #Find the smallest number between the old and next number. 
        delete_item = min(delete_item, item[1])
#print the smallest number
print (delete_item)