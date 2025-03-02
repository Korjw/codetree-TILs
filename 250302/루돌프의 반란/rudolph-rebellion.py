N, M, P, C, D = map(int,input().split())

rudol = list(map(int,input().split()))
rudol[0], rudol[1] = rudol[0] - 1, rudol[1] - 1
rudol.append(-1)

santa = []
grid = [[[0,0] for _ in range(N)] for __ in range(N)]
remove_santa_list = []
stun_santa_list = []
score = [0 for _ in range(P+1)]


for _ in range(P):
    sn, sr, sc = map(int,input().split())
    santa.append([sn, sr-1, sc-1])
    grid[sr-1][sc-1] = [sn,0]
santa.sort()

def select_santa_num():
    temp_list = []
    for st in santa:
        if st[0] not in remove_santa_list:
            temp_list.append([(st[1] - rudol[0]) * (st[1] - rudol[0]) + (st[2] - rudol[1]) * (st[2] - rudol[1]), st[1], st[2], st[0]])
    temp_list.sort(key = lambda x : (x[0], -x[1], -x[2]))
    
    if not len(temp_list):
        return []
    #print(1232, temp_list)
    return [temp_list[0][3], temp_list[0][1], temp_list[0][2]]

rdx, rdy = [-1,0,1,1,1,0,-1,-1], [-1,-1,-1,0,1,1,1,0]

def select_rudol_dir(sn):
    if rudol[0] == santa[sn][1]:
        if rudol[1] < santa[sn][2]: # 오른쪽
            return 5
        else: # 왼쪽
            return 1
    elif rudol[1] == santa[sn][2]:
        if rudol[0] > santa[sn][1]: # 위쪽
            return 7
        else: # 아래쪽
            return 3
    else:
        if rudol[0] < santa[sn][1] and rudol[1] < santa[sn][2]: # 오른쪽 아래 대각선
            return 4
        elif rudol[0] < santa[sn][1] and rudol[1] > santa[sn][2]: # 왼쪽 아래 대각선
            return 2
        elif rudol[0] > santa[sn][1] and rudol[1] < santa[sn][2]: # 오른쪽 위 대각선
            return 6
        else: # 왼쪽 위 대각선
            return 0

sdx, sdy = [-1,0,1,0], [0,1,0,-1] #상우하좌

def select_santa_dir(i, sn):    
    temp_list = []
    count = 0
    for dx, dy in zip(sdx, sdy):
        x, y = santa[i][1] + dx, santa[i][2] + dy
        if not out_of_range(x,y) and not grid[x][y][0]:
            if (x - rudol[0]) * (x - rudol[0]) + (y - rudol[1]) * (y - rudol[1]) <= (santa[i][1] - rudol[0]) * (santa[i][1] - rudol[0]) + (santa[i][2] - rudol[1]) * (santa[i][2] - rudol[1]):
                temp_list.append([(x - rudol[0]) * (x - rudol[0]) + (y - rudol[1]) * (y - rudol[1]), count])
        count+=1
    temp_list.sort()

    if len(temp_list) == 0:
        return
    #print(temp_list)
    x, y = santa[i][1] + sdx[temp_list[0][1]], santa[i][2] + sdy[temp_list[0][1]]
    #print(567,santa[i],x,y, temp_list)
    grid[santa[i][1]][santa[i][2]] = [0,0]
    santa[i][1], santa[i][2] = x, y
    grid[x][y] = [sn, temp_list[0][1]]
    

def out_of_range(x, y):
    return x < 0 or y < 0 or x > N-1 or y > N-1

def santa_move():
    for i, st in enumerate(santa):
        if st[0] not in remove_santa_list and [st[0],1] not in stun_santa_list and [st[0],2] not in stun_santa_list:
            select_santa_dir(i, st[0])
    return

def rudol_crash(x,y,direction,t,stun_yn,score_yn):
    if grid[x][y][0]:
        santa_idx = santa.index([grid[x][y][0], x, y])
        move_x, move_y = x + rdx[direction] * t, y + rdy[direction] * t
        if score_yn:
            score[santa[santa_idx][0]] += t
        if stun_yn:
            stun_santa_list.append([santa[santa_idx][0],2])
        #print(76,x,y,direction, move_x, move_y,t)
        if out_of_range(move_x, move_y):
            remove_santa_list.append(santa[santa_idx][0])
            return
        santa[santa_idx][1], santa[santa_idx][2] = move_x, move_y
        if grid[move_x][move_y][0]:
            santa_crash(move_x, move_y, direction,1,0,0,'r')
    return

def santa_crash(x,y,direction,t,stun_yn,score_yn,rs):
    #상호작용은 score x
    if grid[x][y][0]:
        santa_idx = santa.index([grid[x][y][0], x, y])
        if direction == -1:
            direction = (grid[x][y][1] + 2) % 4
        #print(direction)
        if rs == 'r':
            move_x, move_y = x + rdx[direction] * t, y + rdy[direction] * t
        else:
            move_x, move_y = x + sdx[direction] * t, y + sdy[direction] * t
        if score_yn:
            score[santa[santa_idx][0]] += t
        if stun_yn:
            stun_santa_list.append([santa[santa_idx][0],2])
        #print(54,x,y,direction, move_x, move_y,t)
        if out_of_range(move_x, move_y):
            remove_santa_list.append(santa[santa_idx][0])
            return
        santa[santa_idx][1], santa[santa_idx][2] = move_x, move_y
        if grid[move_x][move_y][0]:
            santa_crash(move_x, move_y, direction,1,0,0,'s')

    return

def make_grid():
    global grid
    grid = [[[0,0] for _ in range(N)] for __ in range(N)]

    for st in santa:
        if st[0] not in remove_santa_list:
            grid[st[1]][st[2]] = [st[0], 0]

def stun_check():
    temp_list = []
    for i in range(len(stun_santa_list)):
        stun_santa_list[i][1] -= 1
        if stun_santa_list[i][1] == 0:
            temp_list.append(stun_santa_list[i])

    for temp in temp_list:
        stun_santa_list.remove(temp)

    return

def plus_score():
    for st in santa:
        if st[0] not in remove_santa_list:
            score[st[0]] += 1

for _ in range(M):
    stun_check()
    # 스턴 -1하고 0이면 제거
    santa_num = select_santa_num()
    rudol_dir = -1
    if len(santa_num):
        rudol_dir = select_rudol_dir(santa.index(santa_num))
        rudol[2] = rudol_dir
        #print(santa_num, rudol_dir, santa.index(santa_num))

    if rudol_dir != -1 and not out_of_range(rudol[0]+rdx[rudol_dir], rudol[1]+rdy[rudol_dir]):
        rudol[0], rudol[1] = rudol[0]+rdx[rudol_dir], rudol[1]+rdy[rudol_dir]

    rudol_crash(rudol[0], rudol[1],rudol[2],C,1,1)
    make_grid()

    santa_move()

    santa_crash(rudol[0], rudol[1],-1,D,1,1,'s')
    make_grid()

    plus_score()
    # 점수 기록

# print()
# for i in range(N):
#     for j in range(N):
#         print(grid[i][j], end = ' ')
#     print()

# print(rudol, santa)
# print(remove_santa_list)
# print(stun_santa_list)
for i in range(1, len(score)):
    print(score[i], end = ' ')