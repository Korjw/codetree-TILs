from collections import deque
n = int(input())

grid = [list(map(int,input().split())) for _ in range(n)]
robot = [0, 0]

for i in range(n):
    for j in range(n):
        if grid[i][j] == 9:
            robot[0], robot[1] = i, j
            grid[i][j] = 0

level = 2
level_count = 0
time = 0
dx, dy = [-1,0,1,0], [0,-1,0,1]
visited = [[False for _ in range(n)] for __ in range(n)]
q = deque()
try_list = []

def init():
    global visited, q, try_list
    visited = [[False for _ in range(n)] for __ in range(n)]
    q = deque()
    try_list = []
    return

def out_of_range(x,y):
    return x < 0 or y < 0 or x > n-1 or y > n-1

def bfs(x, y):
    visited[x][y] = True
    q.append([0, x, y])
    while q:
        dist, curr_x, curr_y = q.popleft()
        for dir_x, dir_y in zip(dx, dy):
            if not out_of_range(curr_x+dir_x, curr_y+dir_y) and grid[curr_x+dir_x][curr_y+dir_y] <= level and not visited[curr_x+dir_x][curr_y+dir_y]:
                visited[curr_x+dir_x][curr_y+dir_y] = True
                q.append([dist+1, curr_x+dir_x, curr_y+dir_y])
                if grid[curr_x+dir_x][curr_y+dir_y] < level and grid[curr_x+dir_x][curr_y+dir_y]:
                    try_list.append([dist+1, curr_x+dir_x, curr_y+dir_y])

def kill(x,y,t):
    global robot, level, level_count,time
    robot[0], robot[1] = x, y
    grid[x][y] = 0
    level_count += 1
    time += t
    if level == level_count:
        level += 1
        level_count = 0

while True:
#for _ in range(1):
    bfs(robot[0], robot[1])
    try_list.sort()
    if try_list:
        kill(try_list[0][1], try_list[0][2], try_list[0][0])
    else:
        break
    init()

#print(try_list,robot)
#print(robot,level,level_count,time)
print(time)
