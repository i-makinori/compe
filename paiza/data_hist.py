# https://paiza.jp/student/challenges/43/retry

import functools
import operator
prod = functools.partial(functools.reduce, operator.mul)


import string


def decode(char, parsed, code):
    if code == "":
        return parsed
    elif code[0] == char:
        return decode(char, parsed+char, code[1:])
    elif code[0] == '(':
        return decode(char, parsed+"(", code[1:])
    elif code[0] == ')':
        return decode(char, parsed+")", code[1:])
    elif code[0].isdigit() :
        return decode(char, parsed+code[0], code[1:])
    
    else:
        if parsed[-1].isdigit :
            return decode(char, parsed+" ", code[1:])
        else:
            return decode(char, parsed, code[1:])
        

import operator
import functools




        
def to_num(char, stack, code, nest=0, last_digit=False):
    # print(char, stack, code)
    if code == "" :
        return 0
    elif code[0].isdigit() :
        i = 0
        while code[0:i+1].isdigit() and i<100000:
            i = i+1
        return to_num(char, [int(code[0:i])] + stack, code[i:], nest+1, last_digit=True)
    elif code[0] == char:
        num = prod(stack+[1])
        if last_digit :
            return num + to_num(char, stack[1:], code[1:], nest-1)
        else :
            return num + to_num(char, stack, code[1:], nest)
        # return num + to_num(char, stack, code[1:], nest)
    elif code[0] == '(':
        return to_num(char, stack, code[1:], nest)
    elif code[0] == ')':
        return to_num(char, stack[1:], code[1:], nest-1)
    elif code[0] == ' ':
        if last_digit :
            return to_num(char, stack[1:], code[1:], nest-1)
        else :
            return to_num(char, stack, code[1:], nest)
    else :
        return 0


        # return to_num(char, stack + [num], code)
        
str1 = "abcdefg10h12(ij2(3k))l9mnop4(3(2(6(qq)r)s5tu)7v5w)x15(yz)"
str2 = "10000(10000(10000(2000(ab)500(dz)c200h)2mu3000(fpr)))"

# decode('a', "", code_string)

def get_num(char ,code):
    return to_num(char, [] , decode(char, " ", code))

def test_dict(code):
    list(map(lambda c:
             print(c, to_num(c, [] , decode(c , " ", code))),
             string.ascii_lowercase))

code_string = input()

test_dict(code_string)
