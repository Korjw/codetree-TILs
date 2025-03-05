N,M,F = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(N)]

east = [list(map(int,input().split())) for _ in range(M)]
west = [list(map(int,input().split())) for _ in range(M)]
south = [list(map(int,input().split())) for _ in range(M)]
north = [list(map(int,input().split())) for _ in range(M)]
top = [list(map(int,input().split())) for _ in range(M)]
time_grid = []
#남동서북
dir_x, dir_y = [0,0,1,-1], [1,-1,0,0]
#동서남북

for i in range(M):
    temp = []
    for item in west[i]:
        temp.append(item)
    for item in south[i]:
        temp.append(item)
    for item in east[i]:
        temp.append(item)
    for item in north[i]:
        temp.append(item)
    time_grid.insert(0,temp[:])

strange = []
for _ in range(F):
    r,c,d,v = map(int,input().split())
    strange.append([r,c,d,v])

curr_x,curr_y,curr_h = 0,0,0

for i in range(M):
    for j in range(M):
        if top[i][j] == 2:
            curr_x, curr_y, curr_h = i, j, M

exit = [-1,-1]

for i in range(N):
    for j in range(N):
        if grid[i][j] == 4:
            exit = [i,j]

time_x, time_y = -1, -1
for i in range(N):
    for j in range(N):
        if grid[i][j] == 3:
            time_x, time_y = i, j
            break
    if time_x != -1:
        break

def out_of_range(x,y,h):
    return x < 0 or y < 0 or x > N-1 or y > N-1 or h < -1 or h > M

def top_out_of_range(x,y,h):
    return x < 0 or y < 0 or x > M-1 or y > M-1
    
def convert(x):
    if x == -1:
        return 4*M-1
    elif x == 4*M:
        return 0
    else:
        return x

def move_strange(t):
    for i, st in enumerate(strange):
        if (t+1) % strange[i][3] == 0:
            move_x, move_y = strange[i][0]+dir_x[strange[i][2]], strange[i][1]+dir_y[strange[i][2]]
            if not out_of_range(move_x, move_y, 0) and grid[move_x][move_y] == 0:
                grid[move_x][move_y] = 6
                grid[strange[i][0]][strange[i][1]] = 0
                strange[i][0], strange[i][1] = move_x, move_y
#서남동북

def move_low_1(x,y,d):
    if x == -1:
        return [4 * M - 1 - y, 22]
    if y == -1:
        return [x,22]
    if x == M:
        return [y+M,22]
    if y == M:
        return [(3 * M - 1 - x),22]

def move_low_2(x):
    if x >= 0 and x <= M-1:
        return [time_x+x, time_y-1]
    if x >= M and x <= 2*M-1:
        return [time_x+M, time_y+(x-M)]
    if x >= 2*M and x <= 3*M-1:
        return [time_x+(3*M-1-x), time_y+M]
    if x >= 3*M and x <= 4*M-1:
        return [time_x-1, time_y+(4*M-1-x)]
    return


def move_low_3(x):
    if x >= 0 and x <= M-1:
        return [x,0]
    if x >= M and x <= 2*M-1:
        return [M-1, x-M]
    if x >= 2*M and x <= 3*M-1:
        return [3*M-1-x , M-1]
    if x >= 3*M and x <= 4*M-1:
        return [0, 4*M-1-x]
    return

def move_low_4(x,y):
    if y == time_y-1:
        return [x-time_x, 22]
    if x == time_x+M:
        return [M+(y-time_y),22]
    if y == time_y+M:
        return [(3*M-1-(x-time_x)),22]
    if x == time_x-1:
        return [(4*M-1-(y-time_y)),22]

def move_pos():
    global pos, visited
    temp = []
    for item in pos:
        x,y,h = item[0], item[1], item[2]
        #print(h)
        if h == M:
            count = 0
            for dx, dy in zip(dir_x, dir_y):
                move_x, move_y = x+dx, y+dy
                #print(move_x, move_y)
                if top_out_of_range(move_x, move_y, M):
                    move_x, move_y = move_low_1(move_x,move_y,count) # 위치 구하기
                    #print(move_x, move_y)
                    if time_grid[M-1][move_x] == 0 and not visited[move_x][move_y][M-1]:
                        visited[move_x][move_y][M-1] = True
                        temp.append([move_x, move_y, M-1])
                else:
                    if top[move_x][move_y] == 0 and not visited[move_x][move_y][M]:
                        visited[move_x][move_y][M] = True
                        temp.append([move_x, move_y, M]) 
                count += 1

        if h < M and h > 0:
            dir_hx, dir_hh = [-1,1,0,0], [0,0,-1,1]
            for dx, dh in zip(dir_hx, dir_hh):
                move_x, move_h = convert(x + dx), h + dh
                #print(move_x, move_h)
                if move_h == M:
                    move_x, move_y = move_low_3(move_x)
                    if top[move_x][move_y] == 0 and not visited[move_x][move_y][move_h]:
                        visited[move_x][move_y][move_h] = True
                        temp.append([move_x, move_y, move_h])
                elif time_grid[move_h][move_x] == 0 and not visited[move_x][y][move_h]:
                    visited[move_x][y][move_h] = True
                    temp.append([move_x, y, move_h])

        if h == 0:
            count = 0
            dir_hx, dir_hh = [-1,1,0], [0,0,-1]
            for dx, dh in zip(dir_hx, dir_hh):
                move_x, move_y, move_h = convert(x + dx), y, h + dh
                if move_h == -1:
                    move_x, move_y = move_low_2(move_x)
                    #print(214354,move_x,move_y)
                    if not out_of_range(move_x,move_y, move_h) and (grid[move_x][move_y] == 0 or grid[move_x][move_y] == 4) and not visited[move_x][move_y][M+1]:
                        visited[move_x][move_y][M+1] = True
                        temp.append([move_x, move_y, -1])
                else:
                    if time_grid[move_h][move_x] == 0 and not visited[move_x][move_y][move_h]:
                        visited[move_x][move_y][move_h] = True
                        temp.append([move_x, move_y, move_h])
        
        if h == -1:
            for dx, dy in zip(dir_x, dir_y):
                move_x, move_y, move_h = x + dx, y + dy, -1
                if not out_of_range(move_x, move_y, move_h) and grid[move_x][move_y] == 3:
                    move_x, move_y = move_low_4(x, y)
                    if not visited[move_x][move_y][0]:
                        visited[move_x][move_y][0] = True
                        temp.append([move_x, move_y, 0])

                elif not out_of_range(move_x, move_y, move_h) and (grid[move_x][move_y] == 0 or grid[move_x][move_y] == 4) and not visited[move_x][move_y][M+1]:
                    visited[move_x][move_y][M+1] = True
                    temp.append([move_x, move_y, move_h])
    
    pos = temp[:]
    #print(temp)

pos = [[curr_x, curr_y, curr_h]]
visited = [[[False for _ in range(100)] for __ in range(100)] for ___ in range(100)]

visited[curr_x][curr_y][curr_h] = True

def check():
    for ps in pos:
        if [ps[0],ps[1]] == exit and ps[2] == -1:
            return True
    return False

for st in strange:
    grid[st[0]][st[1]] = 6

result = 0
for i in range(2500):
    move_strange(i)
    move_pos()
    tuple_arr = [tuple(j) for j in pos]
    temp_set = set(tuple_arr)
    pos = [list(j) for j in temp_set]
    #print(pos)
    if not len(pos):
        result = -1
        break
    if check():
        result = i + 1
        break
print(result)

# print(time_grid)
# for i in range(N):
#     for j in range(N):
#         print(grid[i][j], end = ' ')
#     print()

# print(strange, time_x, time_y)
# print(top, exit)
# print(pos)