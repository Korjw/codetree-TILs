n, m = map(int,input().split())

grid = [ list(map(int,input().split())) for _ in range(n)]
init_grid = [[0 for _ in range(m)] for __ in range(n)]
m_horse = []
o_horse = []

for i in range(n):
    for j in range(m):
        if grid[i][j] >= 1 and grid[i][j] <= 5:
            m_horse.append([i,j,grid[i][j]])
        init_grid[i][j] = grid[i][j]

pos = []
pos_list = []

result = 0

def make_pos(cnt):
    if cnt == len(m_horse):
        pos_list.append(pos[:])
        return
    
    for i in range(4):
        pos.append(i)
        make_pos(cnt+1)
        pos.pop()

make_pos(0)
dir_x1, dir_y1 = [[-1],[1],[0],[0]], [[0],[0],[-1],[1]]
dir_x2, dir_y2 = [[0,0],[-1,1],[0,0],[-1,1]], [[-1,1],[0,0],[-1,1],[0,0]]
dir_x3, dir_y3 = [[-1,0],[0,1],[1,0],[0,-1]], [[0,1],[1,0],[0,-1],[-1,0]]
dir_x4, dir_y4 = [[0,-1,0],[-1,0,1],[0,1,0],[1,0,-1]], [[-1,0,1],[0,1,0],[1,0,-1],[0,-1,0]]
dir_x5, dir_y5 = [[-1,1,0,0],[-1,1,0,0],[-1,1,0,0],[-1,1,0,0]], [[0,0,-1,1],[0,0,-1,1],[0,0,-1,1],[0,0,-1,1]]
dir_x, dir_y = [dir_x1,dir_x2,dir_x3,dir_x4,dir_x5], [dir_y1,dir_y2,dir_y3,dir_y4,dir_y5]

def out_of_range(x,y):
    return x < 0 or y < 0 or x > n-1 or y > m-1

def make_grid(poss):
    for i, p in enumerate(poss):
        dir_xx, dir_yy = dir_x[m_horse[i][2]-1], dir_y[m_horse[i][2]-1]
        
        for dx, dy in zip(dir_xx[p], dir_yy[p]):
            for k in range(max([n,m])):
                move_x, move_y = m_horse[i][0]+dx*k, m_horse[i][1]+dy*k
                if out_of_range(move_x, move_y):
                    break
                elif grid[move_x][move_y] == 6:
                    break
                else:
                    grid[move_x][move_y] = m_horse[i][2]

result = 2500

def check():
    global result
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                count += 1
    if result > count:
        result = count

def init():
    for i in range(n):
        for j in range(m):
            grid[i][j] = init_grid[i][j]
for poss in pos_list:
    init()
    make_grid(poss)
    check()

print(result)

# for i in range(n):
#     for j in range(m):
#         print(grid[i][j], end = ' ')
#     print()
