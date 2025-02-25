from collections import deque

N, M, P, C, D = map(int,input().split())

rudol = list(map(int,input().split()))
rudol[0], rudol[1] = rudol[0] - 1, rudol[1] - 1

santa = []
grid = [[0 for _ in range(N)] for __ in range(N)]
remove_santa_list = []

for _ in range(P):
    sn, sr, sc = map(int,input().split())
    santa.append([sn, sr-1, sc-1])
    grid[sr-1][sc-1] = sn
santa.sort()

def select_santa_num():
    temp_list = []
    for st in santa:
        temp_list.append([(st[1] - rudol[0]) * (st[1] - rudol[0]) + (st[2] - rudol[1]) * (st[2] - rudol[1]), st[1], st[2], st[0]])
    temp_list.sort(key = lambda x : (x[0], -x[1], -x[2]))
    
    if not len(temp_list):
        return []
    print(temp_list)
    return [temp_list[0][3], temp_list[0][1], temp_list[0][2]]

rdx, rdy = [-1,0,1,1,1,0,-1,-1], [-1,-1,-1,0,1,1,1,0]

def select_rudol_dir(sn):
    if rudol[0] == santa[sn][1]:
        if rudol[1] < santa[sn][2]: # 오른쪽
            return 5
        else: # 왼쪽
            return 1
    elif rudol[1] == santa[sn][2]:
        if rudol[0] < santa[sn][1]: # 위쪽
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

sdx, sdy = [-1,1,0,0], [0,0,-1,1]

def select_santa_dir(sn):
    sn=sn-1
    if rudol[0] == santa[sn][1]:
        if rudol[1] < santa[sn][2]: # 왼쪽
            return [2]
        else: # 오른쪽
            return [3]
    elif rudol[1] == santa[sn][2]:
        if rudol[0] < santa[sn][1]: # 위쪽
            return [0]
        else: # 아래쪽
            return [1]
    else:
        if rudol[0] < santa[sn][1] and rudol[1] < santa[sn][2]: # 왼쪽 위 대각선
            return [0,2]
        elif rudol[0] < santa[sn][1] and rudol[1] > santa[sn][2]: # 오른쪽 위
            return [0,3]
        elif rudol[0] > santa[sn][1] and rudol[1] < santa[sn][2]: # 왼쪽 아래
            return [1,2]
        else: # 오른쪽 아래 대각선
            return [1,3]

def out_of_range(x, y):
    return x < 0 or y < 0 or x > N-1 or y > N-1

def santa_move():
    for st in santa:
        # 기절여부
        st_dir = select_santa_dir(st[0])
    return

santa_num = select_santa_num()
rudol_dir = -1
if len(santa_num):
    rudol_dir = select_rudol_dir(santa.index(santa_num))

print(santa_num, rudol_dir, santa.index(santa_num))

if rudol_dir != -1 and not out_of_range(rudol[0]+rdx[rudol_dir], rudol[1]+rdy[rudol_dir]):
    rudol[0], rudol[1] = rudol[0]+rdx[rudol_dir], rudol[1]+rdy[rudol_dir]


for i in range(N):
    for j in range(N):
        print(grid[i][j], end = ' ')
    print()

print(rudol, santa)