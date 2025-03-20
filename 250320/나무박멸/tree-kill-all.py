n, m, k, c = map(int,input().split())

grid = [list(map(int,input().split())) for __ in range(n)]
next_grid = [[0 for _ in range(n)] for __ in range(n)]
dead_grid = [[0 for _ in range(n)] for __ in range(n)]

def out_of_range(x,y):
    return x < 0 or y < 0 or x > n-1 or y > n-1

def grow_1():
    dir_x, dir_y = [-1,1,0,0], [0,0,-1,1]
    for i in range(n):
        for j in range(n):
            if grid[i][j] < 1:
                continue
            cnt = 0
            for dx, dy in zip(dir_x, dir_y):
                move_x, move_y = i+dx, j+dy
                if not out_of_range(move_x, move_y) and grid[move_x][move_y] > 0:
                    cnt += 1
            grid[i][j] += cnt

def grow_2():
    dir_x, dir_y = [-1,1,0,0], [0,0,-1,1]
    for i in range(n):
        for j in range(n):
            if grid[i][j] < 1:
                continue
            cnt = 0
            for dx, dy in zip(dir_x, dir_y):
                move_x, move_y = i+dx, j+dy
                if not out_of_range(move_x, move_y) and grid[move_x][move_y] == 0 and dead_grid[move_x][move_y] == 0:
                    cnt += 1
            if cnt == 0:
                continue
            grow_cnt = grid[i][j] // cnt
            for dx, dy in zip(dir_x, dir_y):
                move_x, move_y = i+dx, j+dy
                if not out_of_range(move_x, move_y) and grid[move_x][move_y] == 0 and dead_grid[move_x][move_y] == 0:
                    next_grid[move_x][move_y] += grow_cnt

def next_grid_to_grid():
    global grid, next_grid
    grid = [[0 for _ in range(n)] for __ in range(n)]
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]
    next_grid = [[0 for _ in range(n)] for __ in range(n)]

def grid_to_next_grid():
    global grid, next_grid
    next_grid = [[0 for _ in range(n)] for __ in range(n)]
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = grid[i][j]  

def select_dead():
    max_cnt, max_x, max_y = -1, -1, -1
    dir_x, dir_y = [-1,1,1,-1], [-1,-1,1,1]
    for i in range(n):
        for j in range(n):
            if grid[i][j] < 1:
                continue
            cnt = grid[i][j]
            for dx, dy in zip(dir_x, dir_y):
                for l in range(1,k+1):
                    move_x, move_y = i+dx*l, j+dy*l
                    if not out_of_range(move_x, move_y) and grid[move_x][move_y] > 0:
                        cnt += grid[move_x][move_y]
                    else:
                        break
            if max_cnt < cnt:
                max_x, max_y = i, j
                max_cnt = cnt
    
    if max_x == -1:
        return
    dead(max_x, max_y)

result = 0
def dead(x,y):
    global result
    result += grid[x][y]
    grid[x][y] = 0
    dead_grid[x][y] = c

    dir_x, dir_y = [-1,1,1,-1], [-1,-1,1,1]
    for dx, dy in zip(dir_x, dir_y):
        for l in range(1,k+1):
            move_x, move_y = x+dx*l, y+dy*l
            if not out_of_range(move_x, move_y) and grid[move_x][move_y] > 0:
                result += grid[move_x][move_y]
                grid[move_x][move_y] = 0
                dead_grid[move_x][move_y] = c
            elif not out_of_range(move_x, move_y) and grid[move_x][move_y] < 0:
                dead_grid[move_x][move_y] = c
                break
            else:
                break

def dead_low():
    for i in range(n):
        for j in range(n):
            if dead_grid[i][j]:
                dead_grid[i][j] -= 1

for _ in range(m):
    grow_1()
    grid_to_next_grid()
    grow_2()
    next_grid_to_grid()
    dead_low()
    select_dead()

# for i in range(n):
#     for j in range(n):
#         print(grid[i][j], end = ' ')
#     print()           

# print()

# for i in range(n):
#     for j in range(n):
#         print(dead_grid[i][j], end = ' ')
#     print()         
print(result)