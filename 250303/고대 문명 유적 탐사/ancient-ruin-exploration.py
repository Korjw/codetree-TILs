from collections import deque

K, M = map(int,input().split())

grid = [list(map(int,input().split())) for __ in range(5)]

tre_list = list(map(int,input().split()))
select_grid = [[ 0 for _ in range(3)] for __ in range(3)]
rotate_grid = [[ 0 for _ in range(5)] for __ in range(5)]
result_list = []
result = 0

count = 1
result_count = 0

rotation_list = []
dx, dy = [-1,1,0,0], [0,0,-1,1]

def out_of_range(x,y):
    return x < 0 or y < 0 or x > 4 or y > 4

def select_rotation(x,y):
    global select_grid, rotate_grid, visited, count, result_count, check_list
    select_grid = [[ 0 for _ in range(3)] for __ in range(3)]
    for i in range(5):
        for j in range(5):
            rotate_grid[i][j] = grid[i][j]

    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            select_grid[i-x+1][j-y+1] = grid[i][j]
    
    for i in range(3):
        check_list = []
        result_count = 0
        select_grid = list(map(list, zip(*select_grid[::-1])))
        
        for k in range(x-1,x+2):
            for l in range(y-1,y+2):
                rotate_grid[k][l] = select_grid[k-x+1][l-y+1]
        
        for k in range(5):
            for l in range(5):
                if [k,l] not in check_list:
                    count = 1
                    visited = [[False for _ in range(5)] for __ in range(5)]
                    check(k,l,rotate_grid[k][l])
                    if count >= 3:
                        result_count += count

        rotation_list.append([result_count,i,x,y])

def check(x,y,value):
    global count
    visited[x][y] = True
    check_list.append([x,y])
    #print(x,y,value)

    for dir_x, dir_y in zip(dx,dy):
        move_x, move_y = x + dir_x, y + dir_y

        if not out_of_range(move_x, move_y) and not visited[move_x][move_y] and rotate_grid[move_x][move_y] == value:
            check(move_x,move_y,value)
            count+=1

def rotate(x,y,rotate_cnt):
    global select_grid, rotate_grid, visited, count, grid, result
    select_grid = [[ 0 for _ in range(3)] for __ in range(3)]
    remove_list = []

    for i in range(5):
        for j in range(5):
            rotate_grid[i][j] = grid[i][j]

    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            select_grid[i-x+1][j-y+1] = grid[i][j]
    
    for i in range(rotate_cnt+1):
        select_grid = list(map(list, zip(*select_grid[::-1])))
    
    for k in range(x-1,x+2):
        for l in range(y-1,y+2):
            rotate_grid[k][l] = select_grid[k-x+1][l-y+1]
        
    for k in range(5):
        for l in range(5):
            count = 1
            visited = [[False for _ in range(5)] for __ in range(5)]
            check(k,l,rotate_grid[k][l])
            if count >= 3:
                remove_list.append([k,l])

    remove_list.sort(key = lambda x : (x[1], -x[0]))
    for remove_pos in remove_list:
        rotate_grid[remove_pos[0]][remove_pos[1]] = tre_list[0]
        del tre_list[0]
    
    result += len(remove_list)

    #print(remove_list)

def check(x,y,value):
    global count
    visited[x][y] = True
    check_list.append([x,y])
    #print(x,y,value)

    for dir_x, dir_y in zip(dx,dy):
        move_x, move_y = x + dir_x, y + dir_y

        if not out_of_range(move_x, move_y) and not visited[move_x][move_y] and rotate_grid[move_x][move_y] == value:
            check(move_x,move_y,value)
            count+=1

def chain():
    global visited, count, rotate_grid, grid, result

    remove_list = []
    
    for i in range(5):
        for j in range(5):
            rotate_grid[i][j] = grid[i][j]

    for k in range(5):
        for l in range(5):
            count = 1
            visited = [[False for _ in range(5)] for __ in range(5)]
            check(k,l,rotate_grid[k][l])
            if count >= 3:
                remove_list.append([k,l])

    remove_list.sort(key = lambda x : (x[1], -x[0]))
    for remove_pos in remove_list:
        grid[remove_pos[0]][remove_pos[1]] = tre_list[0]
        del tre_list[0]
    if len(remove_list) > 0:
        result += len(remove_list)
        #print(remove_list)
        chain()

for _ in range(K):
    result = 0
    rotation_list = []

    for i in range(1,4):
        for j in range(1,4):
            select_rotation(i,j)

    rotation_list.sort(key = lambda x : (-x[0], x[1], x[3], x[2]))
    #print(rotation_list)
    if rotation_list[0][0] == 0:
        break
    rotate(rotation_list[0][2], rotation_list[0][3], rotation_list[0][1])
    for i in range(5):
        for j in range(5):
            grid[i][j] = rotate_grid[i][j]
    chain()

    if result:
        result_list.append(result)

# for i in range(5):
#     for j in range(5):
#         print(rotate_grid[i][j], end = ' ')
#     print()
# print()
# for i in range(5):
#     for j in range(5):
#         print(grid[i][j], end = ' ')
#     print()
for item in result_list:
    print(item, end = ' ')