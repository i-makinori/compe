# https://paiza.jp/student/challenges/183/retry


def abc_string(k):
    if k == 0:
        return ""
    elif k == 1:
        return "ABC"
    else :
        return "A" + abc_string(k-1) + "B" + abc_string(k-1) + "C"


def len_abc_string(k):
    if k<=0:
        return 0
    elif k==1:
        return 3
    else:
        return 3+2*len_abc_string(k-1)
    

    
def zoom(k,s,t):
    
def input_test():
    i1, i2, i3 = input().rstrip().split(' ')
    k, s, t = int(i1), int(i2)-1, int(i3)-1

    print(zoom(k,s,t))
    
digit = 7


