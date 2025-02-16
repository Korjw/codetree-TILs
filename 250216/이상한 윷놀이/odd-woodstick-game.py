n, k = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(n)]
horse_grid = [[ [] for _ in range(n)] for __ in range(n)]
horse_list = []
dx, dy = [0,0,-1,1], [1,-1,0,0] # 0 오른쪽 1 왼쪽 2 위쪽 3 아래쪽

for i in range(k):
    x,y,d = map(int,input().split())
    horse_grid[x-1][y-1].append([i,x-1,y-1,d-1])
    horse_list.append([i,x-1,y-1,d-1])

def out_of_range(x,y):
    return x < 0 or y < 0 or x > n-1 or y > n-1

def turn(d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    else:
        return 2

# 0 오른쪽 1 왼쪽 2 위쪽 3 아래쪽
def move():
    for i, horse in enumerate(horse_list):
        x = horse[1]
        y = horse[2]
        direction = horse[3]
        idx = horse_grid[x][y].index([i,x,y,direction])
        # horse grid도 같이 바꿔줌
        if out_of_range(x+dx[direction], y+dy[direction]): # 바깥쪽
            move_blue(i,x,y,idx)
        elif not out_of_range(x+dx[direction], y+dy[direction]) and grid[x+dx[direction]][y+dy[direction]] == 0: # 흰색 안쪽
            move_white(i,x,y,idx,direction)
        elif not out_of_range(x+dx[direction], y+dy[direction]) and grid[x+dx[direction]][y+dy[direction]] == 1: # 빨간색 안쪽
            move_red(i,x,y,idx,direction)
        elif not out_of_range(x+dx[direction], y+dy[direction]) and grid[x+dx[direction]][y+dy[direction]] == 2: # 파란색 안쪽
            move_blue(i,x,y,idx)
            
        if len(horse_grid[horse_list[i][1]][horse_list[i][2]]) >= 4:
            return True
        
    return False   
def move_white(i,x,y,idx,direction):
    remove_list = []
    for riding_horse in range(idx,len(horse_grid[x][y])):
        # horse_grid[x][y][riding_horse][0]는 horse grid의 타있는 말의 번호
        horse_list[horse_grid[x][y][riding_horse][0]][1] = x+dx[direction]
        horse_list[horse_grid[x][y][riding_horse][0]][2] = y+dy[direction]
        remove_list.append(horse_grid[x][y][riding_horse])
        horse_grid[x+dx[direction]][y+dy[direction]].append(horse_list[horse_grid[x][y][riding_horse][0]])
    for item in remove_list:
        horse_grid[x][y].remove(item)

def move_red(i,x,y,idx,direction):
    remove_list = []
    insert_pos = len(horse_grid[x+dx[direction]][y+dy[direction]])
    for riding_horse in range(len(horse_grid[x][y])-1, idx-1, -1):
        # horse_grid[x][y][riding_horse][0]는 horse grid의 타있는 말의 번호
        horse_list[horse_grid[x][y][riding_horse][0]][1] = x+dx[direction]
        horse_list[horse_grid[x][y][riding_horse][0]][2] = y+dy[direction]
        remove_list.append(horse_grid[x][y][riding_horse])
        horse_grid[x+dx[direction]][y+dy[direction]].insert(insert_pos, horse_list[horse_grid[x][y][riding_horse][0]])
        insert_pos+=1
    for item in remove_list:
        horse_grid[x][y].remove(item)

def move_blue(i,x,y,idx):
    blue_horese_idx = horse_grid[x][y].index(horse_list[i])
    horse_list[i][3] = turn(horse_list[i][3])
    direction = horse_list[i][3]
    if not out_of_range(x+dx[direction], y+dy[direction]) and grid[x+dx[direction]][y+dy[direction]] == 2:
        horse_grid[x][y][blue_horese_idx][3] = direction
        return
    if out_of_range(x+dx[direction], y+dy[direction]):
        horse_grid[x][y][blue_horese_idx][3] = direction
        return
    if not out_of_range(x+dx[direction], y+dy[direction]) and grid[x+dx[direction]][y+dy[direction]] == 1: # 빨간색 안쪽
        move_red(i,x,y,idx,direction)
        return
    remove_list = []
    for riding_horse in range(idx,len(horse_grid[x][y])):
        # horse_grid[x][y][riding_horse][0]는 horse grid의 타있는 말의 번호
        horse_list[horse_grid[x][y][riding_horse][0]][1] = x+dx[direction]
        horse_list[horse_grid[x][y][riding_horse][0]][2] = y+dy[direction]
        remove_list.append(horse_grid[x][y][riding_horse])
        horse_grid[x+dx[direction]][y+dy[direction]].append(horse_list[horse_grid[x][y][riding_horse][0]])
    for item in remove_list:
        horse_grid[x][y].remove(item)

count = 0
result = -1
while True:
    count += 1
    if move():
        result = count
        break
    if count > 1000:
        break

# 0 오른쪽 1 왼쪽 2 위쪽 3 아래쪽
print(result)
# print(horse_list)
# print()
# for i in range(n):
#     for j in range(n):
#         print(horse_grid[i][j], end = ' ')
#     print()

# 5 7
# 0 2 0 1 0
# 2 0 0 0 0
# 1 1 1 0 1
# 0 2 0 0 0
# 1 0 2 0 1
# 2 2 1
# 5 2 4
# 1 3 2
# 2 4 1
# 2 3 3
# 1 1 3
# 3 3 2

# 3 4
# 0 2 0
# 0 0 0
# 0 1 0
# 2 1 1
# 2 1 3
# 2 1 2
# 2 1 1