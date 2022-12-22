#Read puzzle input, striping white space and splitting moves by new line. 
with open("puzzle_input.txt") as f:
    moves = f.read().strip().split("\n")

#define puzzle start point for head and tail
head_x, head_y = 0, 0
tail_x, tail_y = 0, 0


#touching

#movement dictionary
mm = {
    "R": [1,0],
    "U": [0,1],
    "L": [-1,0],
    "D": [0,-1]
}
