# faller simulation
# https://paiza.jp/student/challenges/123/retry


i1, i2, i3 = input().rstrip().split(' ')
height, width, num = int(i1), int(i2), int(i3)

block_dict = list(range(num))
for i in range(num):
    s = input().rstrip().split(' ')
    block_dict[i] = {"hei": int(s[0]), "wid":int(s[1]), "x_left":int(s[2])}

bottom = height-1

space = '.'
filled = '#'

field = [[space for i in range(width)] for j in range(height)]


def dict_list_to_str(height, width, block_list):
    field = [['.']*width]*height
    for line in field :
        print(''.join(line))


def if_intersect(a, b):
    return bool(list(set(a) & set(b)))

def if_overlap(line, test):
    for i in test:
        if line[i]==filled :
            return False
    return True

def fill_by_block(field, x_left, y_top, block_width, block_height):
    for y in range(y_top, y_top+block_height):
        for x in range(x_left, x_left+block_width):
            field[y][x] = filled
    return field

def down(field, block):
    x_filled = list(range(block["x_left"], block["x_left"]+block["wid"]))
    block_bottom=0
    # field[block_bottom]
    while block_bottom!=bottom+1 and if_overlap(field[block_bottom], x_filled) :
        block_bottom+=1
    field = fill_by_block(field,
                          block["x_left"], block_bottom - block["hei"],
                          block["wid"], block["hei"])
    return field

def show_field(field):
    for line in field :
        print(''.join(line))

for block in block_dict:
    field = down(field, block)

show_field(field)
