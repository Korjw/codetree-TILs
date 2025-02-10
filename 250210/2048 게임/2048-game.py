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

left()

for i in range(n):
    for j in range(n):
        print(grid[i][j], end = ' ')
    print()