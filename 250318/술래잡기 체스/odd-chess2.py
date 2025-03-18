import copy
import sys

grid =[[[] for _ in range(4)] for __ in range(4)]
grid_list = []
horse_list = []
dx, dy = [-1,-1,0,1,1,1,0,-1], [0,-1,-1,-1,0,1,1,1]

for i in range(4):
    p1,d1,p2,d2,p3,d3,p4,d4 = list(map(int,input().split()))
    grid[i][0] = [p1,d1-1]
    grid[i][1] = [p2,d2-1]
    grid[i][2] = [p3,d3-1]
    grid[i][3] = [p4,d4-1]
    horse_list.append([i,0,p1,d1-1])
    horse_list.append([i,1,p2,d2-1])
    horse_list.append([i,2,p3,d3-1])
    horse_list.append([i,3,p4,d4-1])

sulrae = [[0,0,grid[0][0][1]]] # x 위치, y 위치, 방향
horse_list.remove([0,0,grid[0][0][0],grid[0][0][1]])
score = [grid[0][0][0]]
grid[0][0] = [-1,-1]
total_count = 0
grid_list.append(copy.deepcopy(grid))

# for i in range(4):
#     for j in range(4):
#         print(grid[i][j], end = ' ')
#     print()

def out_of_range(x,y):
    return x < 0 or y < 0 or x > 3 or y > 3

def horse_move():
    for i in range(4):
        for j in range(4):
            for k in range(2):
                grid[i][j][k] = grid_list[-1][i][j][k]

    init_horse()
    horse_list.sort(key = lambda x : x[2])
    n = len(horse_list)
    #print(horse_list)

    for i in range(n):
        x, y, direction = horse_list[i][0], horse_list[i][1], horse_list[i][3]
        count = 0
        for k in range(8):
            d = (direction+k) % 8
            move_x, move_y = x+dx[d], y+dy[d]
            #print(move_x,move_y,sulrae[-1])
            if not out_of_range(move_x, move_y) and grid[move_x][move_y] != [-1,-1] and grid[x][y] != [-1,-1]:
                count = d
                temp_x, temp_y,temp_num,temp_dir = x,y,grid[x][y][0],grid[x][y][1] 
                #print(x,y,move_x,move_y)
                # if [x,y,grid[x][y][0],direction] == [0, 2, 10, 2]:
                #     print(sulrae,grid_list[-1])
                #     print(len(grid_list))
                #     print(horse_list)
                #     sys.exit(0)
                idx = horse_list.index([x,y,grid[x][y][0],direction])
                horse_list[idx] = [move_x, move_y, grid[x][y][0] ,d]
                idx = horse_list.index([move_x,move_y,grid[move_x][move_y][0],grid[move_x][move_y][1]])
                horse_list[idx] = [x,y,grid[move_x][move_y][0], grid[move_x][move_y][1]]
                grid[x][y][0], grid[x][y][1] = grid[move_x][move_y][0], grid[move_x][move_y][1]  
                grid[move_x][move_y][0], grid[move_x][move_y][1] = temp_num, d
                break
        horse_list.sort(key = lambda x : x[2])
        
            #print(i,horse_list,horse_list[i],grid[move_x][move_y], x+dx[4],y+dy[4])
    if [1, 2, 0] in sulrae:
        for l in range(4):
            for m in range(4):
                print(grid[l][m], end =' ')
            print()
    grid_list.append(copy.deepcopy(grid))
        #if i == 4:
            #return

def init_horse():
    global horse_list
    
    horse_list = []
    for i in range(4):
        for j in range(4):
            if grid_list[-1][i][j][0] != -1:
                #if i == 0 and j == 2:
                    #print(i,j,grid_list[-1][i][j][0],grid_list[-1][i][j][1])
                horse_list.append([i,j,grid_list[-1][i][j][0],grid_list[-1][i][j][1]])

result = []

def sulrae_move(end):
    global total_count
    #print(end, sulrae)
    count = 0
    for i in range(1,4):
        curr_x, curr_y, direction = sulrae[-1][0], sulrae[-1][1], sulrae[-1][2]
        x, y = curr_x+dx[direction]*i, curr_y+dy[direction]*i
        if not out_of_range(x,y) and grid_list[-1][x][y] != [-1,-1]:
            count += 1

            horse_move()
            number = grid_list[-1][x][y][0]
            b_direction = grid_list[-1][x][y][1]

            # grid_list.append()

            score.append(grid[x][y][0])
            sulrae.append([x,y,b_direction])            
            # if [0, 1, -1, -1] == [x,y,grid_list[-1][x][y][0],grid_list[-1][x][y][1]]:
            #     print(x,y,grid_list[-1][x][y][0],grid_list[-1][x][y][1],grid_list[-1],sulrae)
            #     return
            horse_list.remove([x,y,grid_list[-1][x][y][0],grid_list[-1][x][y][1]])
            grid_list[-1][x][y] = [-1,-1]

            #print(sulrae,len(grid_list))

            sulrae_move(end)

            grid_list.pop()

            score.pop()
            sulrae.pop()

    #print(456,sum(score))
    result.append(sum(score))


sulrae_move(False)

#print(sulrae)
horse_list.sort(key = lambda x : -x[2])

# for i in range(4):
#     for j in range(4):
#         print(grid[i][j], end = ' ')
#     print()

# print(len(score))
# print(score)
# print(len(horse_list))
# print(horse_list)

print(max(result))








