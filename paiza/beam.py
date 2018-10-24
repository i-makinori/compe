import numpy as np



space = 0
topdown = 1
downtop = 2

space_char = '_'
topdown_char = '\\'
downtop_char = '/'


i1, i2 = input().rstrip().split(' ')
height, width = int(i1), int(i2)

def decode_line(str):
    return(list(map(lambda c :
                    topdown if c == topdown_char else (downtop if c==downtop_char else space)
                    ,str)))

cells_lines = list(range(height))

for i in range(height):
    s = input()
    cells_lines[i] = decode_line(s)

# print(cells_lines)

direction = 0 # to (0:right, 1:down, 2:left, 3:top)
i = 0
current = (0,0) # y,x


def move_on(direction, current):
    if direction == 0 :
        return (current[0], current[1]+1)
    elif direction == 2:
        return (current[0], current[1]-1)
    elif direction == 1:
        return (current[0]+1, current[1])
    elif direction == 3:
        return (current[0]-1, current[1])
    else :
        print("direction_error : ", current, direction)

def rotate(direction, cell):
    if cell == topdown:
        #return (direction+1)%4
        if direction%2 ==0: return (direction+1)%4
        if direction%2 ==1: return (direction-1)%4
    elif cell == downtop:
        #return (direction-1)%4
        if direction%2 ==0: return (direction-1)%4
        if direction%2 ==1: return (direction+1)%4
    else:
        return direction

while current[1] < width and current[1]>=0 and current[0] < height and current[0]>=0 :
    current_cell = cells_lines[current[0]][current[1]]
    # print(i, current_cell, direction,current)

    direction = rotate(direction, current_cell)
    current = move_on(direction,current)
    i = 1+i



# print(current)
print(i)
