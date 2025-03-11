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
    global dow_num
    dow_num = []
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

    for i in range(rx-lx+1):
        for j in range(ry-ly+1):
            print(temp_grid[i][j], end = ' ')
        print()

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

    for i in range(rx-lx+1):
        for j in range(ry-ly+2):
            print(temp_grid[i][j], end = ' ')
        print()

    return True

def roll_up_3(): # 반으로 접어 올리기
    # 반 구하기 뒤집고 그냥 올리기 위에

    # 반 구하기 가로 최대 구하고 그대로 그리드 만들어서 90도 회전 후에 위에 올려버리기
    
    return True


lx,ly,rx,ry = n-1,0,n-1,0
roll_size = 1

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

# 꾹 누르기
# lx,ly,rx,ry 기준
ry = n-1
print(lx,ly,rx,ry)


for i in range(n):
    for j in range(n):
        if len(grid[i][j]) and grid[i][j][1]:
            print(grid[i][j][1], end = ' ')
        else:
            print(0, end = ' ')
    print()
