n,m,k = map(int,input().split())
grid = [list(map(int,input().split())) for __ in range(n)]

air_con = []
office = []
# 좌,상,우,하
for i in range(n):
    for j in range(n):
        if grid[i][j] >= 2:
            air_con.append([i,j,grid[i][j]-2])
        if grid[i][j] == 1:
            office.append([i,j])

air_con_grid = [[[0 for _ in range(n)] for __ in range(n)] for ___ in range(len(air_con))]

wall_list = []

for i in range(m): # s 0 위, 1 왼
    x,y,s = map(int,input().split())
    wall_list.append([i,x-1,y-1,s])

wall_grid = [[0 for _ in range(n)] for __ in range(n)]

for wall in wall_list:
    if wall[3] == 0:
        wall_grid[wall[1]][wall[2]] = 1
        wall_grid[wall[1]-1][wall[2]] = 1
    else:
        wall_grid[wall[1]][wall[2]] = 1
        wall_grid[wall[1]][wall[2]-1] = 1

#---------

def out_of_range(x,y):
    return x < 0 or y < 0 or x > n-1 or y > n-1

def out_of_range2(x):
    return x < 0 or x > n-1

def convert(x):
    if x < 0:
        return 0
    if x > n-1:
        return n-1
    return x

def wind(i,x,y,num,direction):
    if direction == 0: #좌
        dir_wx, dir_wy = [-1,0,1], [-1,-1,-1]
        curr_wall_yn = False
        if wall_grid[x][y]:
            curr_wall_yn = True

        if not out_of_range(x-1,y) and wall_grid[x-1][y] and not out_of_range(x,y-1) and wall_grid[x][y-1] and curr_wall_yn:
            dir_wx, dir_wy = [1], [-1]
        elif not out_of_range(x+1,y) and wall_grid[x+1][y] and not out_of_range(x,y-1) and wall_grid[x][y-1] and curr_wall_yn:
            dir_wx, dir_wy = [-1], [-1]

        elif not out_of_range(x-1,y) and wall_grid[x-1][y] and curr_wall_yn:
            dir_wx, dir_wy = [0,1], [-1,-1]
        elif not out_of_range(x+1,y) and wall_grid[x+1][y] and curr_wall_yn:
            dir_wx, dir_wy = [-1,0], [-1,-1]
        elif not out_of_range(x-1,y-1) and wall_grid[x-1][y-1] and not out_of_range(x-1,y) and wall_grid[x-1][y]:
            dir_wx, dir_wy = [0,1], [-1,-1]
        elif not out_of_range(x,y-1) and wall_grid[x][y-1] and curr_wall_yn:
            dir_wx, dir_wy = [-1,1], [-1,-1]
        elif not out_of_range(x-1,y-1) and wall_grid[x-1][y-1] and not out_of_range(x-1,y) and wall_grid[x-1][y]:
            dir_wx, dir_wy = [-1,0], [-1,-1]

        for wx, wy in zip(dir_wx, dir_wy):
            #print(123,x+wx,y+wy)
            if not out_of_range(x+wx, y+wy):
                air_con_grid[i][x+wx][y+wy] = num

    if direction == 2: # 우
        dir_wx, dir_wy = [-1,0,1], [1,1,1]
        curr_wall_yn = False
        if wall_grid[x][y]:
            curr_wall_yn = True

        if not out_of_range(x-1,y) and wall_grid[x-1][y] and not out_of_range(x,y+1) and wall_grid[x][y+1] and curr_wall_yn:
            dir_wx, dir_wy = [1], [1]
        elif not out_of_range(x+1,y) and wall_grid[x+1][y] and not out_of_range(x,y+1) and wall_grid[x][y+1] and curr_wall_yn:
            dir_wx, dir_wy = [-1], [1]

        elif not out_of_range(x-1,y) and wall_grid[x-1][y] and curr_wall_yn:
            dir_wx, dir_wy = [0,1], [1,1]
        elif not out_of_range(x+1,y) and wall_grid[x+1][y] and curr_wall_yn:
            dir_wx, dir_wy = [-1,0], [1,1]
        elif not out_of_range(x-1,y+1) and wall_grid[x-1][y+1] and not out_of_range(x-1,y) and wall_grid[x-1][y]:
            dir_wx, dir_wy = [0,1], [1,1]
        elif not out_of_range(x,y+1) and wall_grid[x][y+1] and curr_wall_yn:
            dir_wx, dir_wy = [-1,1], [1,1]
        elif not out_of_range(x+1,y+1) and wall_grid[x+1][y+1] and not out_of_range(x+1,y) and wall_grid[x+1][y]:
            dir_wx, dir_wy = [-1,0], [1,1]

        for wx, wy in zip(dir_wx, dir_wy):
            #print(123,x+wx,y+wy)
            if not out_of_range(x+wx, y+wy):
                air_con_grid[i][x+wx][y+wy] = num

    if direction == 1: # 상
        dir_wx, dir_wy = [-1,-1,-1], [-1,0,1]
        curr_wall_yn = False

        if wall_grid[x][y]:
            curr_wall_yn = True
        if not out_of_range(x,y-1) and wall_grid[x][y-1] and not out_of_range(x-1,y) and wall_grid[x-1][y] and curr_wall_yn:
            dir_wx, dir_wy = [-1], [1]
        elif not out_of_range(x,y+1) and wall_grid[x][y+1] and not out_of_range(x-1,y) and wall_grid[x-1][y] and curr_wall_yn:
            dir_wx, dir_wy = [1], [1]
        elif not out_of_range(x,y-1) and wall_grid[x][y-1] and curr_wall_yn:
            #print(1,x,y)
            dir_wx, dir_wy = [-1,-1], [0,1]
        elif not out_of_range(x,y+1) and wall_grid[x][y+1] and curr_wall_yn:
            #print(2,x,y)
            dir_wx, dir_wy = [-1,-1], [-1,0]
        elif not out_of_range(x-1,y-1) and wall_grid[x-1][y-1] and not out_of_range(x,y-1) and wall_grid[x][y-1]:
            #print(3,x,y)
            dir_wx, dir_wy = [-1,-1], [0,1]
        elif not out_of_range(x-1,y) and wall_grid[x-1][y] and curr_wall_yn:
            #print(4,x,y)
            dir_wx, dir_wy = [-1,-1], [-1,1]
        elif not out_of_range(x-1,y+1) and wall_grid[x-1][y+1] and not out_of_range(x,y+1) and wall_grid[x][y+1]:
            #print(5,x,y)
            dir_wx, dir_wy = [-1,-1], [-1,0]

        for wx, wy in zip(dir_wx, dir_wy):
            #print(123,x+wx,y+wy)
            if not out_of_range(x+wx, y+wy):
                air_con_grid[i][x+wx][y+wy] = num

    if direction == 3: #하
        dir_wx, dir_wy = [1,1,1], [-1,0,1]
        curr_wall_yn = False

        if wall_grid[x][y]:
            curr_wall_yn = True
        if not out_of_range(x,y-1) and wall_grid[x][y-1] and not out_of_range(x+1,y) and wall_grid[x+1][y] and curr_wall_yn:
            dir_wx, dir_wy = [1], [1]
        elif not out_of_range(x,y+1) and wall_grid[x][y+1] and not out_of_range(x+1,y) and wall_grid[x+1][y] and curr_wall_yn:
            dir_wx, dir_wy = [1], [-1]
        elif not out_of_range(x,y-1) and wall_grid[x][y-1] and curr_wall_yn:
            #print(1,x,y)
            dir_wx, dir_wy = [1,1], [0,1]
        elif not out_of_range(x,y+1) and wall_grid[x][y+1] and curr_wall_yn:
            #print(2,x,y)
            dir_wx, dir_wy = [1,1], [-1,0]
        elif not out_of_range(x+1,y-1) and wall_grid[x+1][y-1] and not out_of_range(x,y-1) and wall_grid[x][y-1]:
            #print(3,x,y)
            dir_wx, dir_wy = [1,1], [0,1]
        elif not out_of_range(x+1,y) and wall_grid[x+1][y] and curr_wall_yn:
            #print(4,x,y)
            dir_wx, dir_wy = [1,1], [1,1]
        elif not out_of_range(x+1,y+1) and wall_grid[x+1][y+1] and not out_of_range(x,y+1) and wall_grid[x][y+1]:
            #print(5,x,y)
            dir_wx, dir_wy = [1,1], [-1,0]

        for wx, wy in zip(dir_wx, dir_wy):
            #print(123,x+wx,y+wy)
            if not out_of_range(x+wx, y+wy):
                air_con_grid[i][x+wx][y+wy] = num
# 좌,상,우,하
dir_lx, dir_ly, dir_hx, dir_hy = [-1,-1,-1,1],[-1,-1,1,-1], [1,-1,1,1], [-1,1,1,1]

def start_wind():
    for i, air in enumerate(air_con):
        count = 4
        if air[2] == 1:
            curr_lx, curr_ly, curr_hx, curr_hy = air[0]-1, air[1], air[0]-1, air[1]
            air_con_grid[i][curr_lx][curr_ly] = 5
            for k in range(n):
                #print(curr_lx, curr_ly, curr_hx, curr_hy)
                if out_of_range2(curr_lx):
                    break
                curr_lx, curr_ly, curr_hx, curr_hy = convert(curr_lx), convert(curr_ly), convert(curr_hx), convert(curr_hy)
                #print(curr_lx, curr_ly, curr_hx, curr_hy)
                for k in range(curr_lx,curr_hx+1):
                    for j in range(curr_ly, curr_hy+1):
                        #print(456,k,j)
                        if air_con_grid[i][k][j]:
                            wind(i,k,j,count,air[2])
                curr_lx, curr_ly, curr_hx, curr_hy = curr_lx+dir_lx[1], curr_ly+dir_ly[1], curr_hx+dir_hx[1], curr_hy+dir_hy[1]
                count -= 1
        
        elif air[2] == 3:
            curr_lx, curr_ly, curr_hx, curr_hy = air[0]+1, air[1], air[0]+1, air[1]
            air_con_grid[i][curr_lx][curr_ly] = 5
            for k in range(n):
                #print(curr_lx, curr_ly, curr_hx, curr_hy)
                if out_of_range2(curr_lx):
                    break
                curr_lx, curr_ly, curr_hx, curr_hy = convert(curr_lx), convert(curr_ly), convert(curr_hx), convert(curr_hy)
                #print(curr_lx, curr_ly, curr_hx, curr_hy)
                for k in range(curr_lx,curr_hx+1):
                    for j in range(curr_ly, curr_hy+1):
                        #print(456,k,j)
                        if air_con_grid[i][k][j]:
                            wind(i,k,j,count,air[2])
                curr_lx, curr_ly, curr_hx, curr_hy = curr_lx+dir_lx[1], curr_ly+dir_ly[1], curr_hx+dir_hx[1], curr_hy+dir_hy[1]
                count -= 1

        elif air[2] == 0:
            curr_lx, curr_ly, curr_hx, curr_hy = air[0], air[1]-1, air[0], air[1]-1
            air_con_grid[i][curr_lx][curr_ly] = 5
            for k in range(n):
                #print(curr_lx, curr_ly, curr_hx, curr_hy)
                if out_of_range2(curr_ly):
                    break
                curr_lx, curr_ly, curr_hx, curr_hy = convert(curr_lx), convert(curr_ly), convert(curr_hx), convert(curr_hy)
                for k in range(curr_lx,curr_hx+1):
                    for j in range(curr_ly, curr_hy+1):
                        #print(456,k,j)
                        if air_con_grid[i][k][j]:
                            wind(i,k,j,count,air[2])
                curr_lx, curr_ly, curr_hx, curr_hy = curr_lx+dir_lx[0], curr_ly+dir_ly[0], curr_hx+dir_hx[0], curr_hy+dir_hy[0]
                count -= 1

        else: # 2
            curr_lx, curr_ly, curr_hx, curr_hy = air[0], air[1]+1, air[0], air[1]+1
            air_con_grid[i][curr_lx][curr_ly] = 5
            for k in range(n):
                #print(curr_lx, curr_ly, curr_hx, curr_hy)
                if out_of_range2(curr_ly):
                    break
                curr_lx, curr_ly, curr_hx, curr_hy = convert(curr_lx), convert(curr_ly), convert(curr_hx), convert(curr_hy)
                for k in range(curr_lx,curr_hx+1):
                    for j in range(curr_ly, curr_hy+1):
                        #print(456,k,j)
                        if air_con_grid[i][k][j]:
                            wind(i,k,j,count,air[2])
                curr_lx, curr_ly, curr_hx, curr_hy = curr_lx+dir_lx[2], curr_ly+dir_ly[2], curr_hx+dir_hx[2], curr_hy+dir_hy[2]
                count -= 1

def spread():
    dir_x, dir_y = [1,0], [0,1]
    
    for i in range(n):
        for j in range(n):
            curr_wall_yn = False
            if wall_grid[i][j]:
                curr_wall_yn = True
            for dx, dy in zip(dir_x, dir_y):
                tem = result_grid[i][j]

                move_x, move_y = i+dx, j+dy

                if not out_of_range(move_x, move_y):
                    #print(curr_wall_yn, wall_grid[move_x][move_y])
                    if curr_wall_yn and  wall_grid[move_x][move_y]:
                        continue
                    else:
                        #print(i,j,move_x,move_y,result_grid[i][j],result_grid[move_x][move_y])
                        if result_grid[i][j] > result_grid[move_x][move_y]:
                            #print(i,j,move_x,move_y,result_grid[i][j], result_grid[move_x][move_y])
                            p_n_grid[i][j] -= abs(result_grid[i][j] - result_grid[move_x][move_y]) // 4
                            p_n_grid[move_x][move_y] += abs(result_grid[i][j] - result_grid[move_x][move_y]) // 4
                        else:
                            p_n_grid[i][j] += abs(result_grid[i][j] - result_grid[move_x][move_y]) // 4
                            p_n_grid[move_x][move_y] -= abs(result_grid[i][j] - result_grid[move_x][move_y]) // 4

def dis():
    for j in range(n):
        if result_grid[0][j]:
            result_grid[0][j] -= 1
        if result_grid[n-1][j]:
            result_grid[n-1][j] -= 1
        
    for i in range(1,n-1):
        if result_grid[i][0]:
            result_grid[i][0] -= 1
        if result_grid[i][n-1]:
            result_grid[i][n-1] -= 1

def check():
    for of in office:
        if result_grid[of[0]][of[1]] < k:
            return False
    return True

result = 0
result_grid = [[0 for _ in range(n)] for __ in range(n)]
for i in range(102):
    result = i+1
    
    air_con_grid = [[[0 for _ in range(n)] for __ in range(n)] for ___ in range(len(air_con))]

    start_wind()
    for ac in air_con_grid:
        for i in range(n):
            for j in range(n):
                result_grid[i][j] += ac[i][j]

    p_n_grid = [[0 for _ in range(n)] for __ in range(n)]
    spread()

    for i in range(n):
        for j in range(n):
            result_grid[i][j] += p_n_grid[i][j]

    dis()
    if check():
        break
    if result > 100:
        result = -1
        break

print(result)
# print(wall_list)
# print(air_con)

# for i in range(n):
#     for j in range(n):
#         print(air_con_grid[1][i][j], end = ' ')
#     print()
# print()

# for i in range(n):
#     for j in range(n):
#         print(wall_grid[i][j], end = ' ')
#     print()
# print()

# for i in range(n):
#     for j in range(n):
#         print(result_grid[i][j], end = ' ')
#     print()
# print()

# for i in range(n):
    # for j in range(n):
    #     print(p_n_grid[i][j], end = ' ')
    # print()

#4 3 1
# 1 0 0 1 
# 0 0 2 0 
# 0 0 2 0 
# 0 0 0 0 
# 3 1 0
# 2 2 0
# 1 2 1
