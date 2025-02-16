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
            horse_list[i][3] = turn(horse_list[i][3])
            direction = horse_list[i][3]
            remove_list = []
            for riding_horse in range(idx,len(horse_grid[x][y])):
                # horse_grid[x][y][riding_horse][0]는 horse grid의 타있는 말의 번호
                horse_list[horse_grid[x][y][riding_horse][0]][1] = x+dx[direction]
                horse_list[horse_grid[x][y][riding_horse][0]][2] = y+dy[direction]
                remove_list.append(horse_grid[x][y][riding_horse])
                horse_grid[x+dx[direction]][y+dy[direction]].append(horse_list[horse_grid[x][y][riding_horse][0]])
            for item in remove_list:
                horse_grid[x][y].remove(item)

        elif not out_of_range(x+dx[direction], y+dy[direction]) and grid[x+dx[direction]][y+dy[direction]] == 0: # 흰색 안쪽
            remove_list = []
            for riding_horse in range(idx,len(horse_grid[x][y])):
                # horse_grid[x][y][riding_horse][0]는 horse grid의 타있는 말의 번호
                horse_list[horse_grid[x][y][riding_horse][0]][1] = x+dx[direction]
                horse_list[horse_grid[x][y][riding_horse][0]][2] = y+dy[direction]
                remove_list.append(horse_grid[x][y][riding_horse])
                horse_grid[x+dx[direction]][y+dy[direction]].append(horse_list[horse_grid[x][y][riding_horse][0]])
            for item in remove_list:
                horse_grid[x][y].remove(item)

        elif not out_of_range(x+dx[direction], y+dy[direction]) and grid[x+dx[direction]][y+dy[direction]] == 1: # 빨간색 안쪽

            return
        elif not out_of_range(x+dx[direction], y+dy[direction]) and grid[x+dx[direction]][y+dy[direction]] == 2: # 파란색 안쪽
            return

def check():
    for i in range(n):
        for j in range(n):
            if len(horse_grid[i][j]) == 4:
                return True
    return False   
count = 0
result = -1

while True:
    move()
    count += 1
    if check():
        result = count
        break
    if count > 1000:
        break

print(result)
print(horse_list)

for i in range(n):
    for j in range(n):
        print(horse_grid[i][j], end = ' ')
    print()