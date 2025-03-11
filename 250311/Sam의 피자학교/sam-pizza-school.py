n, k = map(int,input().split())
input_dow_list = list(map(int,input().split()))

dow = []
dow_num = []

grid = [[[] for _ in range(n)] for __ in range(n)]

for i, input_dow in enumerate(input_dow_list):
    dow.append([i, input_dow])
    grid[n-1][i] = [i,input_dow]
    dow_num.append(input_dow)

def out_of_range(x,y):
    return x < 0 or y < 0 or x > n-1 or y > n-1

def init_dow():
    global dow_num, dow
    dow_num = []
    dow = []
    for i in range(n):
        dow.append([i,grid[n-1][i][1]])
    for d in dow:
        dow_num.append(d[1])

def plus_dow():
    min_num = min(dow_num)
    for i in range(len(dow)):
        if dow[i][1] == min_num:
            dow[i][1] += 1
            grid[n-1][i][1] += 1

def roll_up_1(lx,ly,rx,ry,roll_size): # 정사각형
    temp_grid = [[[] for _ in range(ry-ly+1)] for __ in range(rx-lx+1)]
    n = len(temp_grid)

    for i in range(rx-lx+1):
        for j in range(ry-ly+1):
            temp_grid[i][j]= grid[lx+i][ly+j]

    temp_grid = list(map(list,zip(*temp_grid[::-1])))

    for i in range(rx-n, rx): # rx -n ~ rx -1
        for j in range(ry+1, ry+n+1): # ry + 1 ~ ry+n
            if out_of_range(i,j):
                return False

    for i in range(rx-n, rx): # rx -n ~ rx -1
        for j in range(ry+1, ry+n+1): # ry + 1 ~ ry+n
            if out_of_range(i,j):
                return False
            grid[i][j] = temp_grid[i+n-rx][j-ry-1]

    # for i in range(rx-lx+1):
    #     for j in range(ry-ly+1):
    #         print(temp_grid[i][j], end = ' ')
    #     print()

def roll_up_2(lx,ly,rx,ry,roll_size): # 직사각형
    temp_grid = [[[] for _ in range(ry-ly+2)] for __ in range(rx-lx+1)]
    n = len(temp_grid[0]) # 가로길이

    for i in range(rx-lx+1):
        for j in range(ry-ly+1):
            temp_grid[i][j+1]= grid[lx+i][ly+j]
    
    temp_grid = list(map(list,zip(*temp_grid[::-1])))
    
    for i in range(rx-n+1, rx): # rx - n + 2 ~ rx -1
        for j in range(ry+1, ry+n+1): # ry + 1 ~ ry+n
            #print(12345,rx-n+1, rx-1, ry+1, ry+n,i,j,i+n-1-rx,j-ry-1)
            if out_of_range(i,j):
                return False

    for i in range(rx-n+1, rx): # rx - n + 2 ~ rx -1
        for j in range(ry+1, ry+n+1): # ry + 1 ~ ry+n
            #print(12345,rx-n+1, rx-1, ry+1, ry+n,i,j,i+n-1-rx,j-ry-1)
            grid[i][j] = temp_grid[i+n-rx][j-ry-1]

    # for i in range(rx-lx+1):
    #     for j in range(ry-ly+2):
    #         print(temp_grid[i][j], end = ' ')
    #     print()

    return True

def roll_up_3(): 
    temp_1 = grid[n-1][:n//2]
    temp_1.reverse()
    k = n // 2
    for item in temp_1:
        grid[n-2][k] = item[:]
        k += 1
    #print(temp_1)
    
    temp_2 = [[[] for _ in range(n//4)] for __ in range(2)]

    for i in range(n-2,n):
        for j in range(n//2, n-n//4): # 4 ~ 5(6)
            temp_2[i-n+2][j-n//2] = grid[i][j][:]
    temp_2[0].reverse()
    temp_2[1].reverse()
    l = 0
    for j in range(n-n//4,n):
        grid[n-3][j] = temp_2[0][l]
        l+=1

    l = 0   
    for j in range(n-n//4,n):
        grid[n-4][j] = temp_2[1][l]     
        l+=1

    return True

def press(lx,ly,rx,ry):
    temp_grid = [[0 for _ in range(n)] for __ in range(n)]
    dir_x, dir_y = [-1,0], [0,-1]
    #print(lx,ly,rx,ry)
    for i in range(lx,rx+1):
        for j in range(ly,ry+1):
            if not len(grid[i][j]):
                #print(123,i,j)
                continue
            a = grid[i][j][1]
            for dx, dy in zip(dir_x, dir_y):
                move_x, move_y = i+dx, j+dy
                if move_x < lx or move_y < ly or move_x > rx or move_y > ry or not len(grid[move_x][move_y]):
                    #print(456,move_x,move_y)
                    continue
                b = grid[move_x][move_y][1]
                #print(i,j,move_x,move_y,temp_grid[i][j],temp_grid[move_x][move_y])
                if a > b:
                    temp_grid[i][j] -= abs(a-b) // 5
                    temp_grid[move_x][move_y] += abs(a-b) // 5
                else:
                    temp_grid[i][j] += abs(a-b) // 5
                    temp_grid[move_x][move_y] -= abs(a-b) // 5

    for i in range(lx,rx+1):
        for j in range(ly,ry+1):
            if temp_grid[i][j]:
                grid[i][j][1] += temp_grid[i][j]
                dow[grid[i][j][0]][1] += temp_grid[i][j]
            
def draw_grid(lx,ly,rx,ry):
    global grid
    temp_grid = [[[] for _ in range(n)] for __ in range(n)]
    for i in range(lx,rx+1):
        for j in range(ly,ry+1):
            temp_grid[i][j] = grid[i][j][:]
    
    grid = [[[] for _ in range(n)] for __ in range(n)]
    
    count = 0

    for j in range(ly,ry+1):
        for i in range(rx,lx-1,-1):
            if len(temp_grid[i][j]):
                grid[n-1][count] = temp_grid[i][j][:]
                count += 1

def check():
    if max(dow_num) - min(dow_num) <= k:
        return True
    return False

result = -1

while True:
    result += 1
    init_dow()
    lx,ly,rx,ry = n-1,0,n-1,0
    roll_size = 1

    #print(dow_num)
    if check():
        break
    
    plus_dow()

    while True:
        if roll_up_1(lx,ly,rx,ry,roll_size) == False:
            break
        lx -= 1
        ly += roll_size
        ry += roll_size
        roll_size += 1
        if roll_up_2(lx,ly,rx,ry,roll_size) == False:
            break
        ly += (roll_size-1)
        ry += roll_size

    ry = n-1
    press(lx,ly,rx,ry)
    draw_grid(lx,ly,rx,ry)

    roll_up_3()
    lx,ly,rx,ry = n-4, n-n//4 ,n-1,n-1
    press(lx,ly,rx,ry)
    draw_grid(lx,ly,rx,ry)

print(result)

# for i in range(n):
#     for j in range(n):
#         if len(grid[i][j]) and grid[i][j][1]:
#             print(grid[i][j], end = ' ')
#         else:
#             print(0, end = ' ')
#     print()

