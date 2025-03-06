from collections import deque

N, M = map(int,input().split())
sr, sc, er, ec = map(int,input().split())
temp_list = list(map(int,input().split()))
temp_cnt = 0
wor_list = []

for i in range(M):
    ar = temp_list[temp_cnt]
    temp_cnt += 1
    ac = temp_list[temp_cnt]
    temp_cnt += 1
    wor_list.append([i,ar,ac])

road_grid = [list(map(int,input().split())) for _ in range(N)]
wor_grid  = [[[] for _ in range(N)] for __ in range(N)]

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
    temp = []
    while (x != er and y != ec) or (x != sr and y != sc):
        print(6546,x,y)
        x,y = next_grid[x][y]
    

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
    temp = []
    wor_count_list = []
    light_grid_list = [] # light 그리드 저장
    count = 0 # 크기 ligth
    for dlx, dly, drx, dry in zip(dir_lx, dir_ly, dir_rx, dir_ry):
        wor_count = 0 # 전사 수
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
                    #print(456,count,lx,j,wor_grid[lx][j])
                    if len(wor_grid[lx][j]):
                        for item in wor_grid[lx][j]:
                            temp.append([count,item])
                        wor_count += len(wor_grid[lx][j])

            if ly == ry:
                if out_of_range_2(ly):
                    #print(count,lx,ly,rx,ry)
                    break
                lx,ly,rx,ry = convert(lx),convert(ly),convert(rx),convert(ry)
                #print(lx,ly,rx,ry)
                for i in range(lx,rx+1):
                    if len(wor_grid[i][ly]):
                        for item in wor_grid[i][ly]:
                            temp.append([count,item])
                        wor_count += len(wor_grid[lx][j])
        wor_count_list.append([wor_count, count])
        count+=1
    
    print(temp)

    return
    

# 출력부
for _ in range(1):
    q = deque()
    visited = [[False for _ in range(N)] for __ in range(N)]
    q.append([sr,sc])
    visited[sr][sc] = True
    select_dir()
    # direction = select_dir()
    # next_grid = [[[] for _ in range(N)] for __ in range(N)]
    # if direction != -1:
    #     sr, sc = sr+dir_x[direction], sc+dir_y[direction]
    # light(sr,sc)



for i in range(N):
    for j in range(N):
        print(wor_grid[i][j], end = ' ')
    print()
print()
for i in range(N):
    for j in range(N):
        print(next_grid[i][j], end = ' ')
    print()
print(sr,sc)