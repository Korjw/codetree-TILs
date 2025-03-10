n,m,k = map(int,input().split())
grid = [list(map(int,input().split())) for __ in range(n)]

air_con = []
# 좌,상,우,하
for i in range(n):
    for j in range(n):
        if grid[i][j] >= 2:
            air_con.append([i,j,grid[i][j]-2])
    print()

air_con_grid = [[[0 for _ in range(n)] for __ in range(n)] for ___ in range(len(air_con))]

wall_list = []

for i in range(m): # s 0 위, 1 왼
    x,y,s = map(int,input().split())
    wall_list.append([i,x-1,y-1,s])

wall_grid = [[2 for _ in range(n)] for __ in range(n)]

for wall in wall_list:
    if wall[3] == 0:
        wall_grid[wall[1]][wall[2]] = wall[3]
        wall_grid[wall[1]-1][wall[2]] = wall[3]
    else:
        wall_grid[wall[1]][wall[2]] = wall[3]
        wall_grid[wall[1]][wall[2]-1] = wall[3]

#---------

def out_of_range(x,y):
    return x < 0 or y < 0 or x > n-1 or y > n-1

def out_of_range2(x):
    return x < 0 or x > n-1

def wind(i,x,y,num,direction):
    if direction == 2:
        dir_wx, dir_wy = [-1,0,1], [0,0,0]
        for wx, wy in zip(dir_wx, dir_wy):
            if not out_of_range(x+wx, y+wy):
                air_con_grid[i][x+wx][x+wy] = num

# 좌,상,우,하
dir_lx, dir_ly, dir_hx, dir_hy = [0,0,-1,0],[0,0,1,0], [0,0,1,0], [0,0,1,0]

def start_wind():
    count = 4
    for i, air in enumerate(air_con):
        if air[2] == 2:
            curr_lx, curr_ly, curr_hx, curr_hy = air[0], air[1]+1, air[0], air[1]+1
            air_con_grid[i][curr_lx][curr_ly] = 5
            for k in range(n):
                if out_of_range2(curr_ly):
                    break
                for i in range(curr_lx,curr_hx+1):
                    for j in range(curr_ly, curr_hy+1):
                        wind(i,curr_x,curr_y,count,air_con[2])
                curr_lx, curr_ly, curr_hx, curr_hy = curr_lx+dir_lx[2], curr_ly+dir_ly[2], curr_hx+dir_hx[2], curr_hy+dir_hy[2]
                count -= 1
            break














for i in range(n):
    for j in range(n):
        print(grid[i][j], end = ' ')
    print()

print()

for i in range(n):
    for j in range(n):
        print(wall_grid[i][j], end = ' ')
    print()