#  최단거리라 함은 상하좌우 인접한 칸 중 이동가능한 칸으로만 이동하여 도달하기까지 거쳐야 하는 칸의 수가 최소가 되는 거리를 뜻합니다.
# 만약 편의점에 도착한다면 해당 편의점에서 멈추게 되고, 
# 이때부터 다른 사람들은 해당 편의점이 있는 칸을 지나갈 수 없게 됩니다. 격자에 있는 사람들이 모두 이동한 뒤에 해당 칸을 지나갈 수 없어짐에 유의합니다.
# 현재 시간이 t분이고 t ≤ m, t번 사람은 자신이 가고 싶은 편의점과 가장 가까이 있는 베이스 캠프에 들어갑니다. 
# 가장 가까운 베이스캠프가 여러 가지인 경우에는 그 중 행이 작은 베이스캠프, 행이 같다면 열이 작은 베이스 캠프로 들어갑니다. 
#  t번 사람이 베이스 캠프로 이동하는 데에는 시간이 전혀 소요되지 않습니다.
# 이때부터 다른 사람들은 해당 베이스 캠프가 있는 칸을 지나갈 수 없게 됩니다.
#  t번 사람이 편의점을 향해 움직이기 시작했더라도 해당 베이스 캠프는 앞으로 절대 지나갈 수 없음에 유의합니다.

n, m = map(int,input().split())
base_grid =[list(map(int,input().split())) for _ in range(n)] # 베이스캠프 그리드
conv_grid = [[0 for _ in range(n)] for __ in range(n)] # 편의점 위치를 표시
valid_grid = [[1 for _ in range(n)] for __ in range(n)]# 갈 수 있는 곳을 표시
dir_x, dir_y = [-1,0,0,1], [0,-1,1,0] #  ↑, ←, →, ↓
base_list = [] # 베이스캠프 위치정보
conv_list = [] # 편의점 번호(1부터 시작), 위치정보

for i in range(n):
    for j in range(n):
        if base_grid[i][j]:
            base_list.append([i, j])

for i in range(m):
    x, y = map(int,input().split())
    x, y = x-1, y-1
    conv_grid[x][y] = 1
    conv_list.append([i+1, x, y])

# m 명의 사람

def in_range(x, y):
    return x > -1 and x < n and y > -1 and y < n

from collections import deque

q = deque()
visited = [[False for _ in range(n)] for __ in range(n)]
base_conv_relation = []

def bfs():
    while(q):
        dist, x, y = q.popleft()
        dist += 1
        for dx, dy in zip(dir_x, dir_y):
            pos_x, pos_y = x + dx, y + dy
            if in_range(pos_x, pos_y) and not visited[pos_x][pos_y] and valid_grid[pos_x][pos_y]:
                q.append([dist, pos_x, pos_y])
                visited[pos_x][pos_y] = True
                if base_grid[pos_x][pos_y]:
                    base_conv_relation.append([dist, pos_x, pos_y])

player_list = []
player = [] # 플레이어번호(1부터 시작), 위치정보
conv_list = [] # 편의점 번호(1부터 시작), 위치정보
valid_grid = [[1 for _ in range(n)] for __ in range(n)]# 갈 수 있는 곳을 표시

def move():
    for p in player_list:
        dist = abs(p[1]-conv[p[0]-1][1]) + abs(p[2]-conv[p[0]-1][2])
        for dx, dy in zip(dir_x, dir_y):
            pos_x, pos_y = p[1] + dx, p[2] + dy
            pos_dist = abs(pos_x-conv[p[0]-1][1]) + abs(pos_y-conv[p[0]-1][2])
            if dist > pos_dist:
                if in_range(pos_x, pos_y) and valid_grid[pos_x][pos_y]:
                    p[1], p[2] = pos_x, pos_y
                elif in_range(pos_x, pos_y) and not valid_grid[pos_x][pos_y]:
                    for i in range(4):
                        pos = []
                        pos_xx, pos_yy = p[1] + dir_x[i], p[2] + dir_y[i]
                        if not (dx == dir_x[i] and dy == dir_y[i]) and not (dx != dir_x[i] and dy == dir_y[i]) and not (dx == dir_x[i] and dy != dir_y[i]):
                            pos.append([abs(pos_xx-conv[p[0]-1][1]) + abs(pos_yy-conv[p[0]-1][2]) ,pos_xx, pos_yy])
                        pos.sort()
                        p[1], p[2] = pos_xx, pos_yy

def check_point():
    return
        
for i in range(m):
    move()
    if len(conv_list) > i:
        conv = conv_list[i]
        q = deque()
        visited = [[False for _ in range(n)] for __ in range(n)]
        q.append([0, conv[1],conv[2]])
        visited[conv[1]][conv[2]] = True
        base_conv_relation = []
        bfs()
        base_conv_relation.sort()
        player = [i+1, base_conv_relation[0][1], base_conv_relation[0][2]]
        player_list.append(player)
    
# 도달 했는지 체크 -> 플레이어 지우고 해당 편의점 비활성화

# 사람들어오면 베이스 캠프 비활성화