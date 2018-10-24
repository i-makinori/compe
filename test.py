# https://paiza.jp/challenges/169/show

test_str1 ="""
2
1 1 1 5 5 5
4 4 4 4 4 4
"""

_x1, _y1, _z1 = 0,1,2
_x2, _y2, _z2 = 3,4,5

_append, _contain, _split, _none = 0,1,2,3

"""
i1 = input() # .rstrip().split(' ')
num = int(i1)

rect_list = list(range(num))

for i in range(num):
    s = input().rstrip().split(' ')

    rect_list[i] = [int(s[0]), int(s[1]), int(s[2]),
                    int(s[0])+int(s[3])-1, int(s[1])+int(s[4])-1, int(s[2])+int(s[5])-1] 
"""


import string

char_dict = string.digits + string.ascii_lowercase
test_2d = [
    [1,1,0, 3,6,0],
    [2,2,0, 5,4,0]]




def col_1d(n1_min, n1_max, n2_min, n2_max):
    # 1:from, 2:to
    print(n1_min, n1_max)
    print(n2_min, n2_max)
    if n1_min<=n2_min and n1_max >= n2_max:
        print("to contains from")
        # return [[n1_min, n1_max, _append]]
        return []
    elif n1_min >= n2_min and n1_max <= n2_max:
        print("from contains to")
        return [[n2_min, n1_min],
                [n1_max, n2_max]]
    elif n1_min <= n2_min and n1_max <= n2_max:
        print("split left")
        return [[n1_min, n2_min]]
                # [n2_min, n1_max]]
    elif n1_min >= n2_min and n1_max >= n2_max:
        print("split right")
        return [[n2_max, n1_max]]
            #[n1_min, n2_max, _split], [n2_max, n1_max, _split]]
    else :
        print("not slitted")
        return [[n1_min, n2_max]]

def append_col_list(list1, list2, list3):
    pass
    
def merge(rect1, rect2):
    # rect1 : from, rect2: to
    x_col = col_1d(rect1[_x1], rect1[_x2], rect2[_x1], rect2[_x2])
    y_col = col_1d(rect1[_y1], rect1[_y2], rect2[_y1], rect2[_y2])
    z_col = col_1d(rect1[_z1], rect1[_z2], rect2[_z1], rect2[_z2])

    
    
    print(x_col)
    print(y_col)
    print(z_col)



    
