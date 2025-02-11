n,m = map(int,input().split())

x, y, d = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(n)]
chk_grid = [[0 for _ in range(m)] for __ in range(n)]

dx, dy = [-1,0,1,0], [0,1,0,-1] # 상 동 남 서

chk_grid[x][y] = 1

def check_move(x,y):
    if chk_grid[x][y] == 1 or grid[x][y] == 1:
        return False
    return True

def move():
    global x,y,d
    move_count = 0
    for _ in range(4):
        d = (d-1) % 4
        if check_move(x+dx[d], y+dy[d]):
            x, y = x+dx[d], y+dy[d]
            chk_grid[x][y] = 1
            return True
        else:
            move_count += 1
    d = (d-2) % 4
    if grid[x+dx[d]][y+dy[d]] == 1:
        return False
    else:
        x, y = x+dx[d], y+dy[d]
        chk_grid[x][y] = 1
        d = (d-2) % 4
        return True

while True:
#for _ in range(9):
    if move() == False:
        break

result = 0

for i in range(n):
    for j in range(m):
        #print(chk_grid[i][j], end = ' ')
        if chk_grid[i][j]:
            result += 1
    #print()
print(result)