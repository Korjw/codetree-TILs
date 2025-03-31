L,N,Q = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(L)]
gisa_grid = [[0 for _ in range(L)] for __ in range(L)]
next_gisa_grid = [[0 for _ in range(L)] for __ in range(L)]
dx,dy = [-1,0,1,0],[0,1,0,-1] # 위,오,아,왼
move_gisa_list = []

dead = []
gisa = []
init_gisa = []
gisa.append([])
init_gisa.append([])
move_pos = True

result = 0
for i in range(N):
    r,c,h,w,k = map(int,input().split())
    r,c = r-1,c-1
    gisa.append([i+1,r,c,h,w,k])
    init_gisa.append([i+1,r,c,h,w,k])
    for k in range(r,r+h):
        for j in range(c,c+w):
            gisa_grid[k][j] = i+1


def out_of_range(x,y):
    return x < 0 or y < 0 or x > L-1 or y > L-1

def grid_to_next_grid():
    global next_gisa_grid
    next_gisa_grid = [[0 for _ in range(L)] for __ in range(L)]
    for i in range(L):
        for j in range(L):
            next_gisa_grid[i][j] = gisa_grid[i][j]


def next_grid_to_grid():
    global gisa_grid
    gisa_grid = [[0 for _ in range(L)] for __ in range(L)]
    for i in range(L):
        for j in range(L):
            gisa_grid[i][j] = next_gisa_grid[i][j]

def move(num,x,y,h,w,d):
    global move_pos
    move_x, move_y = x+dx[d], y+dy[d]
    pos_num = []
    pos = False
    for i in range(move_x+h-1,move_x-1,-1):
        for j in range(move_y+w-1,move_y-1,-1):
            #print(i,j,grid[i][j])
            if out_of_range(i,j) or grid[i][j] == 2:
                move_pos = False
            if not out_of_range(i,j):
                if gisa_grid[i][j] and gisa_grid[i][j] not in pos_num and gisa_grid[i][j] != num:
                    pos_num.append(gisa_grid[i][j])
                    pos = True
                next_gisa_grid[i][j] = num
                if next_gisa_grid[i-dx[d]][j-dy[d]] == num:
                    next_gisa_grid[i-dx[d]][j-dy[d]] = 0
    if pos:
        for number in pos_num:
            if number not in move_gisa_list:
                move_gisa_list.append(number)
            #print(number)
            move(number,gisa[number][1],gisa[number][2],gisa[number][3],gisa[number][4],d)
        
def move_2(num,x,y,h,w,d):
    global move_pos
    move_x, move_y = x+dx[d], y+dy[d]
    pos_num = []
    pos = False
    #print(123,num,x,y,move_x,move_y)
    for i in range(move_x,move_x+h):
        for j in range(move_y,move_y+w):
            #print(i,j,grid[i][j])
            if out_of_range(i,j) or grid[i][j] == 2:
                move_pos = False
            if not out_of_range(i,j):
                if gisa_grid[i][j] and gisa_grid[i][j] not in pos_num and gisa_grid[i][j] != num:
                    pos_num.append(gisa_grid[i][j])
                    pos = True
                next_gisa_grid[i][j] = num
                if next_gisa_grid[i-dx[d]][j-dy[d]] == num:
                    next_gisa_grid[i-dx[d]][j-dy[d]] = 0
    if pos:
        for number in pos_num:
            if number not in move_gisa_list:
                move_gisa_list.append(number)
            #print(number)
            move(number,gisa[number][1],gisa[number][2],gisa[number][3],gisa[number][4],d)

def damage(g):
    cnt = 0
    for i in range(gisa[g][1], gisa[g][1]+gisa[g][3]):
        for j in range(gisa[g][2], gisa[g][2]+gisa[g][4]):
            if grid[i][j] == 1:
                cnt += 1
    #print(cnt)
    if gisa[g][5] <= cnt:
        gisa[g][5] = -1
        for i in range(gisa[g][1], gisa[g][1]+gisa[g][3]):
            for j in range(gisa[g][2], gisa[g][2]+gisa[g][4]):
                next_gisa_grid[i][j] = 0
        dead.append(g)
    else:
        gisa[g][5] -= cnt
    
# 위,오,아,왼

for _ in range(3):
    move_pos = True
    move_gisa_list = []
    grid_to_next_grid()
    i,d = map(int,input().split())

    if i in dead:
        continue
    move_gisa_list.append(i)
    if d == 1 or d == 2:
        move(i,gisa[i][1], gisa[i][2], gisa[i][3], gisa[i][4], d)
    else:
        move_2(i,gisa[i][1], gisa[i][2], gisa[i][3], gisa[i][4], d)

    if move_pos:
        for g in move_gisa_list:
            gisa[g][1], gisa[g][2] = gisa[g][1]+dx[d], gisa[g][2]+dy[d]
            if g != i:
                damage(g)
        next_grid_to_grid()

# for i in range(L):
#     for j in range(L):
#         print(gisa_grid[i][j], end = ' ')
#     print()
# print()
# for i in range(L):
#     for j in range(L):
#         print(grid[i][j], end = ' ')
#     print()
# print()
# for i in range(L):
#     for j in range(L):
#         print(next_gisa_grid[i][j], end = ' ')
#     print()
# print(gisa)
for i,g in enumerate(gisa):
    if i == 0:
        continue
    if g[5] != -1:
       result += init_gisa[g[0]][5] - g[5]
print(result)
