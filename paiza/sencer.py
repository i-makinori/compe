import numpy as np

i1, i2 = input().rstrip().split(' ')
L,D = int(i1), int(i2)
i3 =  input().rstrip()
N = int(i3)

height = D*2+1
width = L+1

circles = np.full((N, 3), 0)

for i in range(N):
    i1, i2,i3 = input().rstrip().split(' ')
    circles[i] = [height-(D+int(i2)+1),int(i1), int(i3)]

start = [D+0, 0]
goal = [D+0, L]

_y,_x,_r=0,1,2
in_circle = 1
out_circle = 0

road = 0
wall = 1


def dist_ratio(y1,x1, y2,x2):
    return (y1-y2)**2+(x1-x2)**2
    
def in_range(y, x, circles):
    return any([(dist_ratio(y,x, c[_y], c[_x]) <= c[_r]**2) for c in circles])

def plot_circles(height, width, circles):
    field = np.full((height, width), 0)

    for y in range(height):
        for x in range(width):
            field[y,x] = in_range(y,x,circles)

    return field

def to_goal(queue, goal,field):
    # print(queue, goal, "\n",field)
    if not(queue) :
        return False
    elif queue[0]==goal:
        return True

    y,x = queue[0][0], queue[0][1]
    hei, wid = field.shape

    if y<0 or y>=hei or x<0 or x>=wid:
        #print("a")
        return to_goal(queue[1:], goal, field)
    elif field[y,x] == wall:
        #print("b", [y,x])
        return to_goal(queue[1:], goal, field)
    else :
        # print("c")
        field[y,x] = wall
        nexts = [[y-1,x-1],[y-1,x],[y-1,x+1],
                 [y,x-1],  [y,x]    ,[y,x+1],
                 [y+1,x-1],[y+1,x]  ,[y+1,x+1]]
        return to_goal(queue[1:] + nexts, goal, field)

circles = np.array([x for x in sorted(circles, key=lambda x: -x[2])])
delete_queue = [[i] for i in range(len(circles))]

searched_list = []


# np.delete(circles, [1,2], axis=0)
while not(to_goal([start] ,goal ,
                  plot_circles(height, width, np.delete(circles, delete_queue[0], axis=0)))):
    nexts = [np.unique(np.append(delete_queue[0], [i])).tolist() for i in range(len(circles))]
    nexts = list(filter(lambda i : not(i in searched_list),
                        nexts))
    searched_list += nexts
    delete_queue = delete_queue[1:] + nexts

print(len(delete_queue[0]))












