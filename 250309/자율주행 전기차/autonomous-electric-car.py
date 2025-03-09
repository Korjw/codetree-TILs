from collections import deque
n,m,c = map(int,input().split())
road_grid = [list(map(int,input().split())) for _ in range(n)]
sg_grid = [[0 for _ in range(n)] for __ in range(n)]
curr_x, curr_y = map(int,input().split())
curr_x, curr_y = curr_x-1, curr_y-1
curr_sg = -1

sg_list = []
remove_list = []

dir_x, dir_y = [-1,1,0,0], [0,0,-1,1]
for i in range(m):
    s_x,s_y,e_x,e_y = map(int,input().split())
    sg_list.append([i+1,s_x-1,s_y-1,e_x-1,e_y-1])

def make_grid():
    for sg in sg_list:
        if sg[0] not in remove_list:
            sg_grid[sg[1]][sg[2]] = sg[0]

def out_of_range(x,y):
    return x < 0 or y < 0 or x > n-1 or y > n-1

def select_sg():
    pos_list = []
    if sg_grid[q[0][0]][q[0][1]]:
        pos_list.append([sg_grid[q[0][0]][q[0][1]], q[0][0], q[0][1], 0])
    while q:
        x,y,dist = q.popleft()
        for dx, dy in zip(dir_x, dir_y):
            move_x, move_y, move_dist = x+dx, y+dy,dist+1
            #print(move_x, move_y)
            if not out_of_range(move_x, move_y) and not vistied[move_x][move_y] and not road_grid[move_x][move_y]:
                if sg_grid[move_x][move_y]:
                    pos_list.append([sg_grid[move_x][move_y], move_x, move_y, move_dist])
                q.append([move_x, move_y,move_dist])
                vistied[move_x][move_y] = True
    #print(pos_list)
    pos_list.sort(key = lambda x : (x[3], x[1], x[2]))

    if not len(pos_list):
        return -1,-1,-1,-1
    return pos_list[0]

def sg_move(start_x, start_y, end_x, end_y):
    global q, vistied
    q = deque()
    vistied = [[False for _ in range(n)] for __ in range(n)]
    q.append([start_x, start_y,0])
    vistied[start_x][start_y] = True
    while q:
        x,y,dist = q.popleft()
        for dx, dy in zip(dir_x, dir_y):
            move_x, move_y, move_dist = x+dx, y+dy,dist+1
            if not out_of_range(move_x, move_y) and not vistied[move_x][move_y] and not road_grid[move_x][move_y]:
                if [move_x, move_y] == [end_x,end_y]:
                    return move_x, move_y, move_dist
                q.append([move_x, move_y,move_dist])
                vistied[move_x][move_y] = True
    return -1,-1,-1
# 4 3 105
while True:
#for _ in range(1):
    sg_grid = [[0 for _ in range(n)] for __ in range(n)]
    make_grid()
    q = deque()
    vistied = [[False for _ in range(n)] for __ in range(n)]
    q.append([curr_x, curr_y,0])
    vistied[curr_x][curr_y] = True
    sg_num, curr_x, curr_y, use_c = select_sg()
    if use_c == -1:
        break
    if use_c > c:
        c -= use_c
        break
    else:
        c -= use_c
    #print(sg_move(sg_list[sg_num-1][1],sg_list[sg_num-1][2],sg_list[sg_num-1][3],sg_list[sg_num-1][4]))
    curr_x, curr_y, use_c = sg_move(sg_list[sg_num-1][1],sg_list[sg_num-1][2],sg_list[sg_num-1][3],sg_list[sg_num-1][4])
    if use_c == -1:
        break
    if use_c > c:
        c -= use_c
        break
    else:
        c += use_c
    remove_list.append(sg_num)

sg_grid = [[0 for _ in range(n)] for __ in range(n)]
make_grid()
if c < 0 or len(remove_list) != len(sg_list):
    print(-1)
else:
    print(c)
# print(curr_x, curr_y, c)
# print(remove_list)
# for i in range(n):
#     for j in range(n):
#         print(sg_grid[i][j], end = ' ')
#     print()
