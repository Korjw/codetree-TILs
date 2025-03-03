R,C,K = map(int,input().split())
R = R + 3
gol = []
dir_x, dir_y = [-1,0,1,0], [0,1,0,-1]
# 북동남서

grid = [[0 for _ in range(C)]for __ in range(R)]
result_x = []

for i in range(K):
    c,d = map(int,input().split())
    gol.append([1,c-1,d])

def out_of_range(x,y):
    return x < 0 or y < 0 or x > R-1 or y > C-1

def west_check(x,y):
    if not out_of_range(x-1,y-1) and not out_of_range(x,y-2) and not out_of_range(x+1,y-1) and not out_of_range(x+2,y-1) and not out_of_range(x+1,y-2):
        if grid[x-1][y-1] == 0 and grid[x][y-2] == 0 and grid[x+1][y-1] == 0 and grid [x+2][y-1] == 0 and grid[x+1][y-2] == 0:
            return True
    return False

def east_check(x,y):
    if not out_of_range(x-1,y+1) and not out_of_range(x,y+2) and not out_of_range(x+1,y+1) and not out_of_range(x+2,y+1) and not out_of_range(x+1,y+2):
        if grid[x-1][y+1] == 0 and grid[x][y+2] == 0 and grid[x+1][y+1] == 0 and grid [x+2][y+1] == 0 and grid[x+1][y+2] == 0:
            return True
    return False

def south_check(x,y):
    if not out_of_range(x+2,y) and not out_of_range(x+1,y-1) and not out_of_range(x+1,y+1):
        if grid[x+2][y] == 0 and grid[x+1][y-1] == 0 and grid[x+1][y+1] == 0:
            return True
    return False

# 북동남서
def move_gol(x,y,i):
    global gol
    curr_x, curr_y = x, y
    #print(i,curr_x,curr_y)
    if south_check(curr_x, curr_y):
        curr_x, curr_y = curr_x+1, curr_y
        gol[i][0], gol[i][1] = curr_x, curr_y
        move_gol(curr_x, curr_y,i)
        return
    if west_check(curr_x,curr_y):
        curr_x, curr_y = curr_x+1, curr_y-1
        gol[i][0], gol[i][1], gol[i][2] = curr_x, curr_y, (gol[i][2] - 1) % 4
        move_gol(curr_x, curr_y,i)
        return
    if east_check(curr_x,curr_y):
        curr_x, curr_y = curr_x+1, curr_y+1
        gol[i][0], gol[i][1], gol[i][2] = curr_x, curr_y, (gol[i][2] + 1) % 4 
        move_gol(curr_x, curr_y,i)
        return

def make_grid(i):
    if gol[i][0]-1 < 3:
        return False

    grid[gol[i][0]-1][gol[i][1]] = i+1
    for j in range(gol[i][1]-1, gol[i][1]+2):
        grid[gol[i][0]][j] = i+1
    grid[gol[i][0]+1][gol[i][1]] = i+1

    grid[gol[i][0]+dir_x[gol[i][2]]][gol[i][1]+dir_y[gol[i][2]]] = (-1) * (i+1)

    return True

move_dx, move_dy = [-1,1,0,0], [0,0,-1,1]
def move(x,y,value,exit_yn):
    global result_x
    visited[x][y] = True
    #print(567,x,y,value,exit_yn)
    result_x.append(x)
    for dx, dy in zip(move_dx, move_dy):
        move_x, move_y = x+dx, y+dy
        if not out_of_range(move_x, move_y) and not visited[move_x][move_y] and not exit_yn:
            #print(move_x,move_y,out_of_range(move_x, move_y),value,grid[move_x][move_y])
            if grid[move_x][move_y] == value:
                move(move_x,move_y,value,0)
                
            elif grid[move_x][move_y] == (-1 * value):
                move(move_x,move_y,value,1)
                
        if not out_of_range(move_x, move_y) and not visited[move_x][move_y] and exit_yn: # 출구에서 이동
            #print(x,y,move_x,move_y,out_of_range(move_x, move_y),value,grid[move_x][move_y])
            if grid[move_x][move_y] and grid[move_x][move_y] != value:
                if grid[move_x][move_y] < 0:
                    move(move_x,move_y,grid[move_x][move_y],1)
                else:
                    move(move_x,move_y,grid[move_x][move_y],0)


# 북동남서   
result = 0
for i in range(K):
    move_gol(0,gol[i][1],i)
    if make_grid(i) == False:
        grid = [[0 for _ in range(C)]for __ in range(R)]
        continue
    visited = [[False for _ in range(C)]for __ in range(R)]
    result_x = []
    move(gol[i][0], gol[i][1], i+1, 0)
    result += (max(result_x) -2)
    
print(result)
#print(gol)
# for i in range(R):
#     for j in range(C):
#         print(grid[i][j], end = ' ')
#     print()

