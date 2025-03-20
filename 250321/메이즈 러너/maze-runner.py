n,m,t = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
player = []
result = 0

for _ in range(m):
    x,y = map(int,input().split())
    if grid[x-1][y-1] == 0:
        grid[x-1][y-1] = 'p'
    else:
        grid[x-1][y-1] += 'p'
    player.append([x-1,y-1])

x,y = map(int,input().split())
grid[x-1][y-1] = 'e'
exit = [x-1,y-1]

def grid_to_next_grid():
    global next_grid 
    
def out_of_range(x,y):
    return x < 0 or y < 0 or x > n-1 or y > n-1

def cal_dist(x1,y1,x2,y2):
    return abs(x1-x2)+ abs(y1-y2)

def move_p():
    global result
    dir_x, dir_y = [-1,1,0,0], [0,0,-1,1]
    for p in player:
        exit_dist = cal_dist(p[0],p[1],exit[0],exit[1])
        for dx, dy in zip(dir_x, dir_y):
            move_x, move_y = p[0]+dx ,p[1]+dy
            if not out_of_range(move_x, move_y) and exit_dist > cal_dist(move_x,move_y,exit[0],exit[1]) and \
            (grid[move_x][move_y] == 0 or 'p' in str(grid[move_x][move_y]) or grid[move_x][move_y] == 'e' or grid[move_x][move_y] == ''):
                #print(grid[p[0]][p[1]], grid[p[0]][p[1]].count('p'))
                result += 1

                if grid[move_x][move_y] == 0:
                    grid[move_x][move_y] = ''
                    grid[move_x][move_y] += 'p'
                elif grid[move_x][move_y] == 'e':
                    grid[p[0]][p[1]] = grid[p[0]][p[1]][:-1]
                    break
                else:
                    grid[move_x][move_y] += 'p'
                grid[p[0]][p[1]] = grid[p[0]][p[1]][:-1]
                break

def select_rotate_pos():
    pos = [[99999,-1,-1,-1,-1]]
    for i in range(n-1):
        for j in range(n-1):
            for k in range(i+1,n):
                for l in range(j+1,n):
                    if (k-i) != (l-j):
                        continue
                    if exit[0] > k or exit[0] < i or exit[1] > l or exit[1] < j:
                        continue
                    is_player = False
                    for o in range(i,k+1):
                        if is_player:
                            break
                        for p in range(j,l+1):
                            if is_player:
                                break
                            if 'p' in str(grid[o][p]):
                                is_player = True
                                pos.append([k-i+1,i,j,k,l])
    pos.sort()
    #print(pos[0])
    return pos[0]

def rotate(pos):
    s,x1,y1,x2,y2 = pos
    if s == 99999:
        return
    temp = [[0 for _ in range(s)] for __ in range(s)]

    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            temp[i-x1][j-y1] = grid[i][j]
    
    # for i in range(s):
    #     for j in range(s):
    #         print(temp[i][j], end = ' ')
    #     print()

    temp = list(map(list,zip(*temp[::-1])))
    
    for i in range(s):
        for j in range(s):
            if isinstance(temp[i][j],int) and temp[i][j] > 0 and temp[i][j] < 10:
                temp[i][j] -= 1
            #print(temp[i][j], end = ' ')
        #print()
    
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            grid[i][j] = temp[i-x1][j-y1]

def set_p_and_e():
    global exit, player
    player = []
    exit = [-1,-1]
    for i in range(n):
        for j in range(n):
            if 'p' in str(grid[i][j]):
                for _ in range(grid[i][j].count('p')):
                    player.append([i,j])
            if grid[i][j] == 'e':
                exit = [i,j]
            if grid[i][j] == '':
                grid[i][j] = 0
    if len(player) == 0:
        return True
    return False
                
for i in range(t):
    move_p()
    rotate(select_rotate_pos())
    if set_p_and_e():
        break
        
print(result)
print(exit[0]+1,exit[1]+1)
# for i in range(n):
#     for j in range(n):
#         print(grid[i][j], end = ' ')
#     print()