n, m, k = map(int,input().split())

gompang = []
gompang_grid = [[[] for _ in range(m)] for __ in range(n)]
dx, dy = [-1,1,0,0], [0,0,1,-1]
result = 0
remove_list = []

for i in range(k):
    x,y,s,d,b = map(int,input().split())
    gompang.append([x-1, y-1, s, d-1, b])
    gompang_grid[x-1][y-1].append([i,b])

def init():
    global gompang_grid, remove_list
    gompang_grid = [[[] for _ in range(m)] for __ in range(n)]
    remove_list = []

def out_of_range(x,y):
    return x < 0 or y < 0 or x > n-1 or y > m-1

def turn(d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    else:
        return 2

def gompang_move():
    global gompang
    for i in range(len(gompang)):
        for _ in range(gompang[i][2]):
            if not out_of_range(gompang[i][0]+dx[gompang[i][3]], gompang[i][1]+dy[gompang[i][3]]):
                gompang[i][0] = gompang[i][0]+dx[gompang[i][3]]
                gompang[i][1] = gompang[i][1]+dy[gompang[i][3]]
            else:  #0 -> 1, 1 -> 0, 2 -> 3, 3 -> 2
                gompang[i][3] = turn(gompang[i][3])
                gompang[i][0] = gompang[i][0]+dx[gompang[i][3]]
                gompang[i][1] = gompang[i][1]+dy[gompang[i][3]]

def make_gompang_grid():
    for i in range(len(gompang)):
        gompang_grid[gompang[i][0]][gompang[i][1]].append([i,gompang[i][4]])

def check_yeol(y):
    global gompang_grid, result
    for x in range(n):
        if len(gompang_grid[x][y]):
            result += gompang_grid[x][y][0][1]
            del gompang[gompang_grid[x][y][0][0]]
            return

def combine_gompang():
    for x in range(n):
        for y in range(m):
            if len(gompang_grid[x][y]) >= 2:
                gompang_grid[x][y].sort(key = lambda x : -x[1])
                for i in range(1,len(gompang_grid[x][y])):
                    remove_list.append(gompang[gompang_grid[x][y][i][0]])

def remove_gompang():
    for item in remove_list:
        gompang.remove(item)

for i in range(m):
    check_yeol(i)
    gompang_move()
    init()
    make_gompang_grid()
    combine_gompang()
    remove_gompang()
    init()
    make_gompang_grid()

print(result)