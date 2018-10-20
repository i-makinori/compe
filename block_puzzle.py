# https://paiza.jp/student/challenges/95/retry

import numpy as np



def flatten(lis):
    return [item for sublist in lis for item in sublist]

def unique_rows(arr):
    if np.array_equal(arr, np.array([])):
        return np.array([])
    elif len(arr)==1:
        return arr
    new_arr = np.array([arr[0]])
    for row in range(1,len(arr)):
        test = map(lambda a : np.array_equal(a, arr[row]),
                   new_arr)
        if any(test):
            pass
        else :
            new_arr = np.concatenate([new_arr, [arr[row]]], axis=0)
    return new_arr



space = 0
filled = 1
FAIL = -1

space_char = ','
filled_char = '#'

field_width = 8 + 3 + 3
shape = np.full((field_width,field_width), 0, dtype=int)
blocks = np.full((4,4,4), 0, dtype=int)



def char_bool(char):
    return (filled if char == filled_char else space)

for i in range(8):
    s = input()
    s = "..."+s+"..."
    shape[i+3] = list(map(lambda x : char_bool(x),s))
for w in range(4) :
    for i in range(4):
        s=input()
        blocks[w,i] = list(map(lambda x : char_bool(x), s))
blocks = sorted(blocks ,key= lambda x : -x.sum())



next_able_shapes = []

def shape_minus(shape1, shape2):
    s1, s2=shape1, shape2

def block_adjust(left, right, top, bottom, block):
    # should : (left + right = top+bottom = block)
    adj_block = block
    # d:delta
    d_left = np.full((4,left), 0, dtype=int)
    d_right = np.full((4,right), 0, dtype=int)
    d_top = np.full((top,field_width), 0, dtype=int)
    d_bottom = np.full((bottom,field_width), 0, dtype=int)

    adj_block = np.hstack((d_left, block, d_right))
    adj_block = np.vstack((d_top, adj_block, d_bottom))

    return adj_block

    
def shape_folds(shape, block):
    foldeds = []
    
    for len_upper_line in range(field_width-4+1):
        len_lower_line = field_width-len_upper_line-4
        for len_left_line in range(field_width-4+1):
            len_right_line = field_width-len_left_line-4
            paper = block_adjust(len_left_line, len_right_line,
                                 len_upper_line, len_lower_line,
                                 block)
            if not np.any(shape-paper==FAIL) :
                foldeds = foldeds + [shape-paper]

    return foldeds


def able_shapes(shape, block):
    rotate_blocks = [np.rot90(block,0), np.rot90(block,1), np.rot90(block,2), np.rot90(block,3)]
    
    able_shapes = flatten(list(map(lambda _block: shape_folds(shape, _block),
                                   rotate_blocks)))

    return able_shapes

able_shapes_list = np.array([shape])
flat_shapes = able_shapes_list
i = 0

while len(flat_shapes) != 0 and i!=4:
    #able_shapes_list = np.unique(flat_shapes
    #,axis=0)
    able_shapes_list = unique_rows(flat_shapes)

    flat_shapes = unique_rows(flatten(list(map(lambda _shape :
                                               able_shapes(_shape, blocks[i]),
                                               able_shapes_list))))
    flat_shapes = np.array([x for x in flat_shapes])

    i = i+1

able_shapes_list = unique_rows(flat_shapes)


if i == 4 and len(flat_shapes)!=0 and np.all(able_shapes_list == space): # np.all(able_shapes_list == 0 :
    print("Yes")
else :
    print("No")

