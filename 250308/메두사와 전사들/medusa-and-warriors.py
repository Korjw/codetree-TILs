from collections import deque

N, M = map(int,input().split())
sr, sc, er, ec = map(int,input().split())
temp_list = list(map(int,input().split()))
temp_cnt = 0
wor_list = []
result = [0, 0, 0]
for i in range(M):
    ar = temp_list[temp_cnt]
    temp_cnt += 1
    ac = temp_list[temp_cnt]
    temp_cnt += 1
    wor_list.append([i,ar,ac])

road_grid = [list(map(int,input().split())) for _ in range(N)]
wor_grid  = [[[] for _ in range(N)] for __ in range(N)]
light_grid = [[0 for _ in range(N)] for __ in range(N)]
stun_wor_list = []

for wor in wor_list:
    wor_grid[wor[1]][wor[2]].append(wor[:])

# 상하좌우
dir_x, dir_y = [-1,1,0,0], [0,0,-1,1]

def out_of_range(x,y):
    return x < 0 or y < 0 or x > N-1 or y > N-1

q = deque()
visited = [[False for _ in range(N)] for __ in range(N)]
next_grid = [[[] for _ in range(N)] for __ in range(N)]
# 맨허튼 거리 = ∣p1−q1∣+∣p2−q2∣
# 상하좌우
# 수정 bfs로 최단 거리 구한다음
# 맨해튼 거리 계산
def select_dir():
    while q:
        x,y = q.popleft()
        for dx, dy in zip(dir_x, dir_y):
            move_x, move_y = x+dx, y+dy
            if not out_of_range(move_x, move_y) and not visited[move_x][move_y] and road_grid[move_x][move_y] == 0:
                q.append([move_x, move_y])
                next_grid[move_x][move_y] = [x, y]
                visited[move_x][move_y] = True
    
    x,y = er,ec
    if not visited[er][ec]:
        return [sr,sc]

    while True:
        if next_grid[x][y] == [sr,sc]:
            break
        x,y = next_grid[x][y]

    return [x, y]

dir_lx, dir_ly, dir_rx, dir_ry = [-1,1,-1,-1], [-1,-1,-1,1], [-1,1,1,1], [1,1,-1,1]

def out_of_range_2(x):
    if x < 0:
        return True
    elif x > N-1:
        return True
    return False

def convert(x):
    if x < 0:
        return 0
    elif x > N-1:
        return N-1
    else:
        return x
    
def light(sr,sc):
    global light_grid
    temp_list = []
    wor_count_list = []
    light_grid_list = [] # light 그리드 저장
    count = 0 # 크기 ligth
    for dlx, dly, drx, dry in zip(dir_lx, dir_ly, dir_rx, dir_ry):
        wor_count = 0 # 전사 수
        temp = []
        lx,ly,rx,ry = sr,sc,sr,sc
        light_grid = [[0 for _ in range(N)] for __ in range(N)]
        for _ in range(N):
            lx,ly,rx,ry = lx+dlx,ly+dly,rx+drx,ry+dry
            if lx == rx:
                if out_of_range_2(lx):
                    #print(count,lx,ly,rx,ry)
                    break
                lx,ly,rx,ry = convert(lx),convert(ly),convert(rx),convert(ry)
                #print(345,count,lx,ly,rx,ry)
                for j in range(ly,ry+1):
                    light_grid[lx][j] = 3

            if ly == ry:
                if out_of_range_2(ly):
                    #print(count,lx,ly,rx,ry)
                    break
                lx,ly,rx,ry = convert(lx),convert(ly),convert(rx),convert(ry)
                #print(lx,ly,rx,ry)
                for i in range(lx,rx+1):
                    light_grid[i][ly] = 3
        
        lx,ly,rx,ry = sr,sc,sr,sc
        for _ in range(N):
            lx,ly,rx,ry = lx+dlx,ly+dly,rx+drx,ry+dry
            if lx == rx:
                if out_of_range_2(lx):
                    #print(count,lx,ly,rx,ry)
                    break
                lx,ly,rx,ry = convert(lx),convert(ly),convert(rx),convert(ry)
                #print(345,count,lx,ly,rx,ry)
                for j in range(ly,ry+1):
                    wor_count += len(wor_grid[lx][j])

                    if light_grid[lx][j] == 2:
                        continue
                    light_grid[lx][j] = 1
                    #print(456,count,lx,j,wor_grid[lx][j])
                    if len(wor_grid[lx][j]):
                        for item in wor_grid[lx][j]:
                            temp.append(item)
                        #print(123,j,sc,lx,sr)
                        
                        if j == sc:
                            if lx > sr:
                                make_shadow(4,lx,j,lx,j)
                            else:
                                make_shadow(0,lx,j,lx,j)
                        elif j < sc:
                            if lx > sr:
                                make_shadow(3,lx+1,j,lx,j)
                            else:
                                make_shadow(1,lx,j,lx-1,j)
                        else:
                            if lx > sr:
                                make_shadow(5,lx+1,j,lx,j)
                            else:
                                make_shadow(7,lx,j,lx-1,j)

                        light_grid[lx][j] = 1

            if ly == ry:
                if out_of_range_2(ly):
                    #print(count,lx,ly,rx,ry)
                    break
                lx,ly,rx,ry = convert(lx),convert(ly),convert(rx),convert(ry)
                #print(lx,ly,rx,ry)
                for i in range(lx,rx+1):
                    wor_count += len(wor_grid[i][ly])
                    if light_grid[i][ly] == 2:
                        continue
                    light_grid[i][ly] = 1
                    if len(wor_grid[i][ly]):
                        for item in wor_grid[i][ly]:
                            temp.append(item)
                        #print(456,i,sr,ly,sc)
                        if i == sr:
                            if ly > sc:
                                make_shadow(6,i,ly,i,ly)
                            else:
                                make_shadow(2,i,ly,i,ly)
                        elif i < sr:
                            if ly > sc:
                                make_shadow(7,i,ly+1,i,ly)
                            else:
                                make_shadow(1,i,ly,i,ly-1)
                        else:
                            if ly > sc:
                                make_shadow(5,i,ly+1,i,ly)
                            else:
                                make_shadow(3,i,ly,i,ly-1)
                        
                        light_grid[i][ly] = 1

        wor_count_list.append([wor_count, count])
        # for i in range(N):
        #     for j in range(N):
        #         print(light_grid[i][j], end = ' ')
        #     print()
        # print()
        light_grid_list.append(light_grid[:][:])
        temp_list.append(temp[:])
        count+=1

    wor_count_list.sort(key = lambda x : (-x[0], x[1]))
    # print(wor_count_list)
    # print(wor_count_list[0][1], light_grid_list[wor_count_list[0][1]])
    # print(temp_list[wor_count_list[0][1]])

    for item in temp_list[wor_count_list[0][1]]:
        stun_wor_list.append(item[0])
    
    result[1] += len(temp_list[wor_count_list[0][1]])
    for i in range(N):
        for j in range(N):
            light_grid[i][j] = light_grid_list[wor_count_list[0][1]][i][j]

    # for i in range(N):
    #     for j in range(N):
    #         print(light_grid[i][j], end = ' ')
    #     print()
    # print()

    return 


dir_slx, dir_sly, dir_srx, dir_sry = [-1,-1,0,0,0,0,0,-1], [0,-1,-1,-1,0,0,0,0], [0,0,0,1,1,1,0,0],[0,0,0,0,0,1,1,1]

def make_shadow(direction, lx, ly, rx, ry):
    global light_grid
    
    #print(direction,lx,ly,rx,ry)
    dlx, dly, drx, dry = dir_slx[direction], dir_sly[direction], dir_srx[direction], dir_sry[direction]
    for _ in range(N):
        lx,ly,rx,ry = lx+dlx,ly+dly,rx+drx,ry+dry

        #print(direction,lx,ly,rx,ry)

        if out_of_range(lx,ly) or out_of_range(rx,ry):
            break
        lx,ly,rx,ry = convert(lx),convert(ly),convert(rx),convert(ry)
        for i in range(lx,rx+1):
            for j in range(ly,ry+1):
                if light_grid[i][j] == 3:
                    light_grid[i][j] = 2

# 맨허튼 거리 = ∣p1−q1∣+∣p2−q2∣
# 상하좌우
# 맨해튼 거리 계산
def move_wor():
    global result
    #print(wor_list, stun_wor_list)
    for i in range(len(wor_list)):
        if wor_list[i][0] in stun_wor_list:
            continue
        dist = abs(sr-wor_list[i][1]) + abs(sc-wor_list[i][2])
        for dx, dy in zip(dir_x, dir_y):
            move_x, move_y = wor_list[i][1]+dx, wor_list[i][2]+dy
            #print(i,move_x, move_y,sr,sc,dist > abs(sr-move_x) + abs(sc-move_y))
            if not out_of_range(move_x, move_y) and light_grid[move_x][move_y] != 1 and dist > abs(sr-move_x) + abs(sc-move_y):
                wor_list[i][1], wor_list[i][2] = move_x, move_y
                result[0] += 1
                break    
    dir_x2, dir_y2 = [0,0,-1,1], [-1,1,0,0]
    for i in range(len(wor_list)):
        if wor_list[i][0] in stun_wor_list:
            continue
        dist = abs(sr-wor_list[i][1]) + abs(sc-wor_list[i][2])
        for dx, dy in zip(dir_x2, dir_y2):
            move_x, move_y = wor_list[i][1]+dx, wor_list[i][2]+dy
            #print(i,move_x, move_y,sr,sc,dist > abs(sr-move_x) + abs(sc-move_y))
            if not out_of_range(move_x, move_y) and light_grid[move_x][move_y] != 1 and dist > abs(sr-move_x) + abs(sc-move_y):
                wor_list[i][1], wor_list[i][2] = move_x, move_y
                result[0] += 1
                break    
    return

def wor_check():
    global result
    remove_list = []

    for i in range(len(wor_list)):
        if wor_list[i][0] in stun_wor_list:
            continue
        x, y = wor_list[i][1], wor_list[i][2]
        if [sr,sc] == [x,y]:
            remove_list.append(wor_list[i])
    
    #print(45,remove_list)
    result[2] += len(remove_list)
    for item in remove_list:
        wor_list.remove(item)
#메두사 이동 후 전사죽음
#전사 이동 후 메두사 공격 후 죽음

def make_grid():
    global wor_grid
    wor_grid  = [[[] for _ in range(N)] for __ in range(N)]
    for wor in wor_list:
        wor_grid[wor[1]][wor[2]].append(wor[:])

while True:
    result = [0,0,0]
    stun_wor_list = []
    q = deque()
    visited = [[False for _ in range(N)] for __ in range(N)]
    q.append([sr,sc])
    visited[sr][sc] = True
    rsr, rsc = select_dir()
    if [sr, sc] == [rsr, rsc]:
        print(-1)
        break
    else:
        sr,sc = rsr, rsc
    for item in wor_grid[sr][sc]:
        wor_list.remove(item)
    make_grid()
    next_grid = [[[] for _ in range(N)] for __ in range(N)]
    light(sr,sc)
    move_wor()
    wor_check()
    make_grid()
    if [sr, sc] == [er, ec]:
        print(0)
        break
    for item in result:
        print(item, end = ' ')
    print()

# 전사이동거리
# 돌 전사
# 공격한 전사
# for i in range(N):
#     for j in range(N):
#         print(wor_grid[i][j], end = ' ')
#     print()
# print()

# print(sr,sc)
