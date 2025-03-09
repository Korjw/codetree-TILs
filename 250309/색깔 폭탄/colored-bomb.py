n, m = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(n)]
temp_grid = [[0 for _ in range(n)] for __ in range(n)]

bomb_list = [[] for _ in range(m)]
temp_list = []
dir_x, dir_y = [-1,1,0,0], [0,0,-1,1]

bomb_count = [[] for _ in range(m)]

def out_of_range(x,y):
    return x < 0 or y < 0 or x > n-1 or y > n-1

def dfs(x,y):
    global temp_list

    for dx, dy in zip(dir_x, dir_y):
        move_x, move_y = x+dx, y+dy
        if not out_of_range(move_x, move_y) and not visited[move_x][move_y] and (grid[move_x][move_y] == grid[x][y] or grid[move_x][move_y] == 0):
            temp_list.append([grid[move_x][move_y], move_x, move_y])
            if grid[move_x][move_y] == 0:
                grid[move_x][move_y] = grid[x][y]
            else:
                visited[move_x][move_y] = True
            dfs(move_x, move_y)

def bomb(bomb_count):
    for item in bomb_count[1]:
        grid[item[1]][item[2]] = -2

def gravity():
    for j in range(n):
        for i in range(n-1,0,-1):
            if grid[i][j] == -2 and grid[i-1][j] != -1:
                grid[i][j] = grid[i-1][j]
                grid[i-1][j] = -2
def clear():
    for i in range(n):
        for j in range(n):
            grid[i][j] = temp_grid[i][j]

result = 0
for k in range(5):
    visited = [[False for _ in range(n)] for __ in range(n)]
    bomb_list = [[] for _ in range(m)]
    temp_list = []

    bomb_count = [[] for _ in range(m)]

    for i in range(n):
        for j in range(n):
            temp_grid[i][j] = grid[i][j]

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and grid[i][j] > 0:
                clear()
                temp_list = [[grid[i][j],i,j]]
                visited[i][j] = True
                dfs(i,j)
                #print(temp_list)
                temp_list.sort(key = lambda x : (-x[0], -x[1], x[2]))
                bomb_list[grid[i][j]-1].append([len(temp_list), temp_list[:][:]])

    if not len(temp_list):
        break

    for i in range(m):
        if len(bomb_list[i]):
            bomb_list[i].sort(key = lambda x : (-x[0], -x[1][0][1], x[1][0][2]))
            bomb_count[i] = bomb_list[i][0][:]
        else:
            bomb_count[i] = [-1,[[-1,-1,-1]]]
    #print(bomb_list)


    bomb_count.sort(key = lambda x : (-x[0], -x[1][0][1], x[1][0][2]))
    #print(bomb_count)

    bomb(bomb_count[0])

    if bomb_count[0][0] <= 1:
        break
    
    result += bomb_count[0][0] * bomb_count[0][0]

    for _ in range(n):
        gravity()

    grid = list(map(list,zip(*grid)))[::-1]

    for _ in range(n):
        gravity()

# for i in range(n):
#     for j in range(n):
#         print(grid[i][j], end = ' ')
#     print()
print(result)