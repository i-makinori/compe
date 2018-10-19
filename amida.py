# https://paiza.jp/student/challenges/20/page/result

i1, i2, i3 = input().rstrip().split(' ')
length, num_vertical_line, line_len = int(i1), int(i2), int(i3)

path_list = [[] for i in range(num_vertical_line)]

for i in range(line_len):
    s = input().rstrip().split(' ')
    from1, from2 = int(s[0])-1, int(s[0])
    to1, to2 = int(s[1]), int(s[2])
    path_list[from1] = path_list[from1] + [(to1 ,to2, from2)]
    path_list[from2] = path_list[from2] + [(to2, to1, from1)]


now_point = (length-1, 0) # y, x

def warp_to(n, warp_points):
    i = 0
    while warp_points[i][0] != n :
        i+=1
    return warp_points[i][1]-1, warp_points[i][2]

def warp (now_point, path_list):
    warp_points =  path_list[now_point[1]]
    if now_point[0]==0 :
        return now_point[1]+1
    if now_point[0] in [way[0] for way in warp_points] :
        warpto = warp_to(now_point[0], warp_points)
        return warp(warpto, path_list)
    else :
        return warp((now_point[0]-1, now_point[1]),
                    path_list)

def recure(now_point, path_list):
    while now_point[0]!=0 :
        warp_points =  path_list[now_point[1]]
        if now_point[0] in [way[0] for way in warp_points] :
            now_point = warp_to(now_point[0], warp_points)
        else :
            now_point = (now_point[0]-1, now_point[1])

    return now_point[1]+1

print(recure(now_point, path_list))
