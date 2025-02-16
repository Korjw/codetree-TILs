N, M = map(int,input().split())

grid = [list(map(str,input())) for _ in range(N)]
red, blue, exit = [0,0], [0,0], [0,0]

init_red, init_blue = [0,0], [0,0]
init_grid = [['' for _ in range(M)] for __ in range(N)]

result = 100
for i in range(N):
    for j in range(M):
        if grid[i][j] == 'R':
            red[0], red[1] = i, j
            init_red[0], init_red[1] = i, j
            
        if grid[i][j] == 'B':
            blue[0], blue[1] = i, j
            init_blue[0], init_blue[1] = i, j

        if grid[i][j] == 'O':
            exit[0], exit[1] = i, j
        
        init_grid[i][j] = grid[i][j]

dx, dy = [0,1,0,-1], [-1,0,1,0]
# 0 좌, 1 하, 2 우, 3 상
try_number = []
try_list = []

def make_try_number(cnt):
    if cnt == 10:
        try_list.append(try_number[:])
        return
    
    for i in range(4):
        try_number.append(i)
        make_try_number(cnt+1)
        try_number.pop()

def init():
    for i in range(N):
        for j in range(M):
            grid[i][j] = init_grid[i][j]
    blue[0], blue[1] = init_blue[0], init_blue[1]
    red[0], red[1] = init_red[0], init_red[1]

def move_marble(marble, move_dir, marble_name):
    exit_check = 0
    curr_x, curr_y = marble[0], marble[1]
    for i in range(max(N, M)):
        if grid[curr_x + dx[move_dir]][curr_y + dy[move_dir]] == 'O':
            grid[curr_x][curr_y] = '.'
            curr_x, curr_y = curr_x + dx[move_dir], curr_y + dy[move_dir]
            exit_check += 1
            break

        if grid[curr_x + dx[move_dir]][curr_y + dy[move_dir]] == '.':
            grid[curr_x][curr_y] = '.'
            curr_x, curr_y = curr_x + dx[move_dir], curr_y + dy[move_dir]
            grid[curr_x][curr_y] = marble_name
        
        else:
            break
    return curr_x, curr_y, exit_check

# 0 좌, 1 하, 2 우, 3 상
def move_first(red, blue, move_dir):
    if red[0] == blue[0] and move_dir == 0:
        if red[1] > blue[1]: # 좌 빨강이 오른쪽일 경우 파랑 먼저
            return 2
        if red[1] < blue[1]:
            return 1

    elif red[0] == blue[0] and move_dir == 2:
        if red[1] > blue[1]: # 우 빨강이 오른쪽일 경우 빨강 먼저
            return 1
        if red[1] < blue[1]:
            return 2

    elif red[1] == blue[1] and move_dir == 3:
        if red[0] > blue[0]: # 상 빨강이 아래일 경우 파랑 먼저
            return 2
        if red[0] < blue[0]:
            return 1

    elif red[1] == blue[1] and move_dir == 1:
        if red[0] > blue[0]: # 하 빨강이 아래일 경우 빨강 먼저
            return 1
        if red[0] < blue[0]:
            return 2
    else:
        return 1

def move(tries):
    global result
    curr_x, curr_y = 0, 0
    bef_move_dir = -1
    red_exit_count, blue_exit_count = 0, 0
    for count, move_dir in enumerate(tries):
        if count >= result or bef_move_dir == move_dir:
            return
            
        if move_first(red, blue, move_dir) == 1:
            red[0], red[1], exit_check = move_marble(red, move_dir, 'R')
            red_exit_count += exit_check
            blue[0], blue[1], exit_check = move_marble(blue, move_dir, 'B')
            blue_exit_count += exit_check
        else:
            blue[0], blue[1], exit_check = move_marble(blue, move_dir, 'B')
            blue_exit_count += exit_check
            red[0], red[1], exit_check = move_marble(red, move_dir, 'R')
            red_exit_count += exit_check

        bef_move_dir = move_dir

        if red_exit_count == 1 and blue_exit_count == 1:
            return
        
        if red_exit_count == 1 and blue_exit_count != 1:
            result = min(result, count+1)
            #print(tries, grid)
            return

make_try_number(0)

#상 0, 하 1, 좌 2, 우3
#try_list = [[2]]
for tries in try_list:
    move(tries)
    #print(grid)
    init()

#print(grid)
#print(red,blue,exit)
if result != 100:
    print(result)
else:
    print(-1)
#print(min(result))