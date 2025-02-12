n,m,h = map(int,input().split())

grid = [[0 for _ in range(n)] for __ in range(h+1)]
line_grid = [[0 for _ in range(n)] for __ in range(h+1)]

try_grid = [[0 for _ in range(n)] for __ in range(h+1)]
try_line_grid = [[0 for _ in range(n)] for __ in range(h+1)]

for _ in range(m):
    a, b = map(int,input().split())
    grid[a][b-1] = 1
    line_grid[a][b-1], line_grid[a][b] = 1, 1

def init():
    for i in range(h+1):
        for j in range(n):
            try_grid[i][j] = grid[i][j]
            try_line_grid[i][j] = line_grid[i][j]

temp_pos = []
temp_line_pos = []
poss_pos = []
poss_line_pos = []
visited = [[False for _ in range(n)] for __ in range(h+1)]

def make_pos(cnt, max_num):
    global temp_pos, temp_line_pos
    if cnt == max_num:
        poss_pos.append(temp_pos[:])
        poss_line_pos.append(temp_line_pos[:])
        return
    
    for i in range(1, h+1):
        for j in range(n):
            if not visited[i][j] and grid[i][j] == 0 and line_grid[i][j] == 0 and [i,j] not in temp_pos and [i,j] not in temp_line_pos and [i,j+1] not in temp_line_pos :
                temp_pos.append([i,j])
                temp_line_pos.append([i,j])
                temp_line_pos.append([i,j+1])
                visited[i][j] = True
                make_pos(cnt+1, max_num)
                temp_pos.pop()
                temp_line_pos.pop()
                temp_line_pos.pop()
                visited[i][j] = False

make_pos(0,1)
temp_pos = []
temp_line_pos = []
make_pos(0,2)
temp_pos = []
temp_line_pos = []
make_pos(0,3)

print(poss_pos)

def simul():
    try_grid = [[0 for _ in range(n)] for __ in range(h+1)]
    try_line_grid = [[0 for _ in range(n)] for __ in range(h+1)]
    # 1. 시뮬레이션 하기 try grid에 그리기

def move():
    # 2. 이동해보고
    가능하면 끝

for i in range(h+1):
    for j in range(n):
        print(grid[i][j], end = ' ')
    print()

print()

for i in range(h+1):
    for j in range(n):
        print(line_grid[i][j], end = ' ')
    print()