n,m,h = map(int,input().split())

grid = [[0 for _ in range(n)] for __ in range(h+1)]
line_grid = [[0 for _ in range(n)] for __ in range(h+1)]

try_grid = [[0 for _ in range(n)] for __ in range(h+1)]
try_line_grid = [[0 for _ in range(n)] for __ in range(h+1)]

for _ in range(m):
    a, b = map(int,input().split())
    grid[a][b-1] = 1
    line_grid[a][b-1], line_grid[a][b] = 1, 1

def init():
    for i in range(h+1):
        for j in range(n):
            try_grid[i][j] = grid[i][j]
            try_line_grid[i][j] = line_grid[i][j]

temp_pos = []
temp_line_pos = []
poss_pos = []
poss_line_pos = []
visited = [[False for _ in range(n)] for __ in range(h+1)]

def make_pos(cnt, max_num):
    global temp_pos, temp_line_pos
    if cnt == max_num:
        poss_pos.append(temp_pos[:])
        poss_line_pos.append(temp_line_pos[:])
        return
    
    for i in range(1, h+1):
        for j in range(n-1):
            if not visited[i][j] and grid[i][j] == 0 and line_grid[i][j+1] == 0 and line_grid[i][j] == 0 and [i,j] not in temp_pos and [i,j] not in temp_line_pos and [i,j+1] not in temp_line_pos :
                temp_pos.append([i,j])
                temp_line_pos.append([i,j])
                temp_line_pos.append([i,j+1])
                visited[i][j] = True
                make_pos(cnt+1, max_num)
                temp_pos.pop()
                temp_line_pos.pop()
                temp_line_pos.pop()
                visited[i][j] = False

#print(poss_pos)

def out_of_range(X,y):
    return y < 0 or y > n-1
def simul(i):
    for x, y in poss_line_pos[i]:
        try_line_grid[x][y] = 1
    
    for x, y in poss_pos[i]:
        try_grid[x][y] = 1

    for l in range(n):
        curr_y = l
        for k in range(h,-1,-1):
            #print(k,curr_y,l,try_line_grid[k][curr_y],try_grid[k][curr_y])
            if try_line_grid[k][curr_y] == 1 and try_grid[k][curr_y] == 1:
                curr_y += 1
            elif not out_of_range(k,curr_y) and try_line_grid[k][curr_y] == 1 and try_grid[k][curr_y-1] == 1:
                curr_y -= 1
        if curr_y != l:
            return False
    return True


result = -1
poss_pos.insert(0, [])
poss_line_pos.insert(0, [])

for k in range(3):
    for i in range(len(poss_pos)):
        init()
        if simul(i):
            result = len(poss_pos[i])
            break
    if result > -1:
        break
    temp_pos = []
    temp_line_pos = []
    poss_pos = []
    poss_line_pos = []
    make_pos(0,k+1)
    #print(poss_pos)

print(result)

# for i in range(h+1):
#     for j in range(n):
#         print(try_line_grid[i][j], end = ' ')
#     print()
