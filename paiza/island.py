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


#

shore = 1
sea = 0

sea_char = '.'
shore_char = '#'



def next_from_neighbors(y, x, height, width, arr):
    center = arr[y,x]
    top = arr[y-1, x] if y!=0 else sea
    bottom = arr[y+1, x] if y!=height-1 else sea
    right = arr[y, x+1] if x!=width-1 else sea
    left = arr[y, x+-1] if x!=0 else sea

    # print([center, top, bottom, right, left])
    return all([center, top, bottom, right, left])
    

def update(island):
    len_y, len_x = island.shape
    # next_isle = np.full((len_y, len_x), 1, dtype=int)
    next_isle = np.copy(island)
    
    #print(next_isle)
    
    for y in range(len_y):
        for x in range(len_x):
            next_isle[y,x] = next_from_neighbors(y,x, len_y, len_x, island)
            
    return next_isle


def char_bool(char):
    return (shore if char == shore_char else sea)


i1, i2 = input().rstrip().split(' ')
height, width = int(i1)+2, int(i2)+2

island = np.full((height, width), 0, dtype=int)

for i in range(height-2):
    s = input()
    island[i+1] = list(map(lambda x : char_bool(x), "."+s+"."))

def n_to_index(n, width):
    return (n%width, int(n/width))
    
coord_tuples = np.full((height, width), 0)
for y in range(height):
    for x in range(width):
        coord_tuples[y,x] = y*width+x
    


    
"""
i = 0
while np.any(island):
    island = update(island)
    # print(island)
    i = i+1

print(i)
"""
