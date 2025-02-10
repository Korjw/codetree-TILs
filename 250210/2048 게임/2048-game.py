n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]

def up():
    for j in range(n):
        for i in range(n-2,-1,-1):
            if grid[i][j] == 0:
                up2(i,j)
def up2(i,j):
    for k in range(i, n-1):
        grid[k][j] = grid[k+1][j]
    grid[n-1][j] = 0

def down():
    for j in range(n):
        for i in range(1,n):
            if grid[i][j] == 0:
                down2(i,j)
def down2(i,j):
    for k in range(i,0,-1):
        grid[k][j] = grid[k-1][j]
    grid[0][j] = 0
    
def right():
    for i in range(n):
        for j in range(1,n):
            if grid[i][j] == 0:
                right2(i,j)
def right2(i,j):
    for l in range(j,0,-1):
        grid[i][l] = grid[i][l-1]
    grid[i][0] = 0

def left():
    for i in range(n):
        for j in range(n-2,-1,-1):
            if grid[i][j] == 0:
                left2(i,j)
def left2(i,j):
    for l in range(j,n-1):
        grid[i][l] = grid[i][l+1]
    grid[i][n-1] = 0

def up_sum():
    #합치기
    for j in range(n):
        for i in range(n-1):
            if grid[i][j] == grid[i+1][j]:
                grid[i][j] *= 2
                grid[i+1][j] = 0
    return

def down_sum():
    #합치기
    for j in range(n):
        for i in range(n-1,0,-1):
            if grid[i][j] == grid[i-1][j]:
                grid[i][j] *= 2
                grid[i-1][j] = 0
    return

def left_sum():
    #합치기
    for i in range(n):
        for j in range(n-1):
            if grid[i][j] == grid[i][j+1]:
                grid[i][j] *= 2
                grid[i][j+1] = 0
    return

def right_sum():
    #합치기
    for i in range(n):
        for j in range(n-1,0,-1):
            if grid[i][j] == grid[i][j-1]:
                grid[i][j] *= 2
                grid[i][j-1] = 0
    return

temp_try = []
try_list = []

def make_try(cnt):
    if cnt == 5:
        try_list.append(temp_try[:])
        return
    
    for i in range(4):
        temp_try.append(i)
        make_try(cnt+1)
        temp_try.pop()

make_try(0)

result = -1
for tries_list in try_list:
    for tries in tries_list:
        max_count = -1
        if tries == 0:
            up()
            up_sum()
            up()
        elif tries == 1:
            down()
            down_sum()
            down()
        elif tries == 2:
            left()
            left_sum()
            left()
        else:
            right()
            right_sum()
            right()
        for i in range(n):
            for j in range(n):
                if max_count < grid[i][j]:
                    max_count = grid[i][j]
        result = max(result, max_count)

print(result)
# 함 이동 -> 합치기 -> 다시 함 이동
