L, N, Q = map(int,input().split())

chess_grid = [list(map(int,input().split())) for __ in range(L)]
gisa_grid = [[-1 for _ in range(L)] for __ in range(L)] # 해당위치 기사 죽은거는 -2
init_gisa_list = []
gisa_list = [] # i, j, h, w, 체력, 기사번호(0부터 시작)

move_list = []
meet_list = []

for i in range(N):
    r, c, h, w, k = map(int,input().split())
    r, c = r-1, c-1
    gisa_list.append([r, c, h, w, k, i])
    init_gisa_list.append([r, c, h, w, k, i])

def full_gisa():
    global gisa_grid
    gisa_grid = [[-1 for _ in range(L)] for __ in range(L)] # 해당위치 기사 죽은거는 -2
    for gisa in gisa_list:
        for i in range(gisa[0], gisa[0]+ gisa[2]):
            for j in range(gisa[1], gisa[1]+gisa[3]):
                gisa_grid[i][j] = gisa[5]
    
dir_x, dir_y = [-1,0,1,0], [0,1,0,-1]

from collections import deque

def in_range(x, y):
    return x > -1 and x < L and y > -1 and y < L

def bfs(start, gisa_number):
    q = deque()
    visited = [[False for _ in range(L)] for __ in range(L)]
    q.append([start[0], start[1]])
    visited[start[0]][start[1]] = True
    result_list = [[start[0], start[1]]]

    while(q):
        x, y = q.popleft()
        for dx, dy in zip(dir_x, dir_y):
            pos_x, pos_y = x + dx, y + dy
            if in_range(pos_x, pos_y) and gisa_grid[pos_x][pos_y] == gisa_number and not visited[pos_x][pos_y]:
                result_list.append([pos_x, pos_y])
                q.append([pos_x, pos_y])
                visited[pos_x][pos_y] = True
    return result_list

def move(gisa, d):
    area = bfs([gisa[0], gisa[1]], gisa[5])

    for a in area:
        check_move(a[0], a[1], d)
    
    #print(meet_list, move_list)
    for meet in meet_list:
        area = bfs([meet[0], meet[1]], meet[2]) # 위치만
        for a in area:
            pos_xx, pos_yy = a[0] + dir_x[d], a[1] + dir_y[d]
            if not in_range(pos_xx, pos_yy) or chess_grid[pos_xx][pos_yy] == 2:
                if meet[2] in move_list:
                    move_list.remove(meet[2])
    
    # print(meet_list, move_list)
    if not move_list:
        return
    gisa[0], gisa[1] = gisa[0] + dir_x[d], gisa[1] + dir_y[d]
    for move_number in move_list:
        gisaa =  gisa_list[move_number]
        gisaa[0], gisaa[1] = gisaa[0] + dir_x[d], gisaa[1] + dir_y[d]
        hit(gisa_list[move_number])
        

def hit(gisa):
    for i in range(gisa[0], gisa[0]+ gisa[2]):
        for j in range(gisa[1], gisa[1]+gisa[3]):
            if chess_grid[i][j] == 1:
                gisa[4] -= 1
        if gisa[4] == 0:
            gisa[5] = -2
            return

def check_move(x, y, d):
    q = deque()
    q.append([x, y])
    result_list = []

    while(q):
        x, y = q.popleft()
        pos_x, pos_y = x + dir_x[d], y + dir_y[d]
        if in_range(pos_x, pos_y) and gisa_grid[pos_x][pos_y] >= 0 and gisa_grid[pos_x][pos_y] != gisa_grid[x][y]:
            meet_list.append([pos_x, pos_y, gisa_grid[pos_x][pos_y]])
            if gisa_grid[pos_x][pos_y] not in move_list:
                move_list.append(gisa_grid[pos_x][pos_y])
                meet_list.append([pos_x, pos_y, gisa_grid[pos_x][pos_y]])
                q.append([pos_x, pos_y])
        else:
            return
    return


full_gisa()
for _ in range(Q):
    move_list = []
    meet_list = []
    i, d = map(int,input().split())
    i = i-1
    move(gisa_list[i], d)
    
    full_gisa()
    # print(gisa_list)
    # for i in range(L):
    #     for j in range(L):
    #         print(gisa_grid[i][j], end = ' ')
    #     print()
result = 0
for i in range(N):
    if gisa_list[i][5] >= 0:
        result += (init_gisa_list[i][4] - gisa_list[i][4])
print(result)