n, m, k = map(int,input().split())

grid = [[[] for _ in range(n)] for __ in range(n)]
next_grid = [[[] for __ in range(n)] for __ in range(n)]

for _ in range(m):
    x,y,m,s,d = map(int,input().split())
    grid[x-1][y-1].append([m,s,d])

dx, dy = [-1,-1,0,1,1,1,0,-1], [0,1,1,1,0,-1,-1,-1]

def out_of_range(x,y):
    curr_x, curr_y = x, y
    if x < 0:
        curr_x = n+x
    if x > n-1:
        curr_x = x-n
    if y < 0:
        curr_y = n+y
    if y > n-1:
        curr_y = y-n

    return curr_x, curr_y

def next_grid_to_grid():
    global grid,next_grid
    grid = [[[] for _ in range(n)] for __ in range(n)]
    for i in range(n):
        for j in range(n):
            if len(next_grid[i][j]):
                for l, item in enumerate(next_grid[i][j]):
                    grid[i][j].append([next_grid[i][j][l][0], next_grid[i][j][l][1], next_grid[i][j][l][2]])

    next_grid = [[[] for __ in range(n)] for __ in range(n)]

def move():
    for i in range(n):
        for j in range(n):
            if len(grid[i][j]):
                for l, item in enumerate(grid[i][j]):
                    curr_x, curr_y, curr_m, curr_s, curr_d = i, j, item[0], item[1] % n, item[2]
                    curr_x, curr_y = out_of_range(curr_x+dx[curr_d] * curr_s, curr_y+dy[curr_d] * curr_s)
                    next_grid[curr_x][curr_y].append([grid[i][j][l][0], grid[i][j][l][1], grid[i][j][l][2]])

def spread():
    for i in range(n):
        for j in range(n):
            if len(grid[i][j]) >= 2:
                dirYn = True
                curr_d = grid[i][j][0][2]
                sum_m = 0
                sum_s = 0
                for item in grid[i][j]:
                    sum_m += item[0]
                    sum_s += item[1]
                    if abs(curr_d - item[2]) % 2 == 1:
                        dirYn = False
                if dirYn:
                    curr_d = 0
                else:
                    curr_d = 1
                sum_m = sum_m // 5
                sum_s = sum_s // len(grid[i][j])
                if sum_m:
                    make_atom(i,j,sum_m,sum_s,curr_d)
            if len(grid[i][j]) == 1:
                next_grid[i][j].append([grid[i][j][0][0], grid[i][j][0][1], grid[i][j][0][2]])
                    
def make_atom(i,j,m,s,d):
    curr_d_cnt = d
    for l in range(0,8,2):
        #print(d+l)
        next_grid[i][j].append([m,s,d+l])

result = 0

def check():
    global result
    for i in range(n):
        for j in range(n):
            if len(grid[i][j]):
                for item in grid[i][j]:
                    result += item[0]

for _ in range(k):
    move()
    next_grid_to_grid()
    spread()
    next_grid_to_grid()

check()
print(result)

# for i in range(n):
#     for j in range(n):
#         print(grid[i][j], end = ' ')
#     print()