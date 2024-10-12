import sys
from collections import deque
n, m, k= map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
attack_list = [[ 0 for _ in range(m)] for __ in range(n)] # 최근 꺼는 앞으로 붙임 insert 0
attacked_list = []
INT_MAX = sys.maxsize

back_x = [[ 0 for _ in range(m)] for __ in range(n)]
back_y = [[ 0 for _ in range(m)] for __ in range(n)]
dir_x, dir_y = [0,1,0,-1], [1,0,-1,0] #우/하/좌/상

def out_of_range(x, y):
    if x < 0:
        x += (n)
    if x > n-1:
        x -= (n)
    if y < 0:
        y += (m)
    if y > m-1:
        y -= (m)
    return x, y

def select_min_potam():
    min_num = INT_MAX
    min_potam = []
    pos_list = []
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                if min_num > grid[i][j]:
                    min_num = grid[i][j]

    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                if min_num == grid[i][j]:
                    pos_list.append([i,j])
    
        max_attack = INT_MAX
        max_row_column_list = INT_MAX
        max_x, max_y = INT_MAX, INT_MAX
        for pos in pos_list:
            if max_attack > attack_list[pos[0]][pos[1]]:
                max_attack = attack_list[pos[0]][pos[1]]
                max_row_column_list = pos[0] + pos[1]
                max_x, max_y = pos[0], pos[1]
            elif max_attack == attack_list[pos[0]][pos[1]]:
                if (pos[0] + pos[1]) < max_row_column_list:
                    max_attack = attack_list[pos[0]][pos[1]]
                    max_row_column_list = pos[0] + pos[1]
                    max_x, max_y = pos[0], pos[1]
                elif (pos[0] + pos[1]) == max_row_column_list:
                    if max_y > pos[1]:
                        max_attack = attack_list[pos[0]][pos[1]]
                        max_row_column_list = pos[0] + pos[1]
                        max_x, max_y = pos[0], pos[1]
    if len(pos_list) >= 2:
        min_attack = -INT_MAX
        min_row_column_list = -INT_MAX
        min_x, min_y = -INT_MAX, -INT_MAX
        for pos in pos_list:
            if min_attack < attack_list[pos[0]][pos[1]]:
                min_attack = attack_list[pos[0]][pos[1]]
                min_row_column_list = pos[0] + pos[1]
                min_x, min_y = pos[0], pos[1]
            elif min_attack == attack_list[pos[0]][pos[1]]:
                if (pos[0] + pos[1]) > min_row_column_list:
                    min_attack = attack_list[pos[0]][pos[1]]
                    min_row_column_list = pos[0] + pos[1]
                    min_x, min_y = pos[0], pos[1]
                elif (pos[0] + pos[1]) == min_row_column_list: 
                    if min_y < pos[1]:
                        min_attack = attack_list[pos[0]][pos[1]]
                        min_row_column_list = pos[0] + pos[1]
                        min_x, min_y = pos[0], pos[1]
        min_potam = [min_x, min_y]

    else:
        min_potam = pos_list[0]
    
    #print(min_num, pos_list, min_potam)
    return min_potam

def select_max_potam(min_potam):
    max_num = -INT_MAX
    max_potam = []
    pos_list = []
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                if max_num < grid[i][j]:
                    max_num = grid[i][j]

    for i in range(n):
        for j in range(m):
            if grid[i][j] and [i,j] != min_potam:
                if max_num == grid[i][j]:
                    pos_list.append([i,j])
    if len(pos_list) >= 2:
        max_attack = INT_MAX
        max_row_column_list = INT_MAX
        max_x, max_y = INT_MAX, INT_MAX
        for pos in pos_list:
            if max_attack > attack_list[pos[0]][pos[1]]:
                max_attack = attack_list[pos[0]][pos[1]]
                max_row_column_list = pos[0] + pos[1]
                max_x, max_y = pos[0], pos[1]
            elif max_attack == attack_list[pos[0]][pos[1]]:
                if (pos[0] + pos[1]) < max_row_column_list:
                    max_attack = attack_list[pos[0]][pos[1]]
                    max_row_column_list = pos[0] + pos[1]
                    max_x, max_y = pos[0], pos[1]
                elif (pos[0] + pos[1]) == max_row_column_list:
                    if max_y > pos[1]:
                        max_attack = attack_list[pos[0]][pos[1]]
                        max_row_column_list = pos[0] + pos[1]
                        max_x, max_y = pos[0], pos[1]
        max_potam = [max_x, max_y]

    else:
        max_potam = pos_list[0]
    
    #print(max_num, pos_list, max_potam)
    return max_potam

def bfs(start, end): 
    q = deque()
    visited = [[ 0 for _ in range(m)] for __ in range(n)]
    q.append([start[0], start[1]])
    visited[start[0]][start[1]]
    end_point_check = False
    
    attacked_list.append(start)

    while(q):
        x, y = q.popleft()
        for dx, dy in zip(dir_x, dir_y):
            pos_x, pos_y = x + dx, y + dy
            pos_x, pos_y = out_of_range(pos_x, pos_y)
            if not visited[pos_x][pos_y] and grid[pos_x][pos_y] > 0:
                q.append([pos_x, pos_y])
                visited[pos_x][pos_y] = True
                back_x[pos_x][pos_y], back_y[pos_x][pos_y] = x, y 
                if pos_x == end[0] and pos_y == end[1]:
                    end_point_check = True
    
    power = grid[start[0]][start[1]]
    grid[end[0]][end[1]] -= power
    attacked_list.append(end)
    if end_point_check:
        back_point = end[:]
        while(1):
            back_point_x = back_x[back_point[0]][back_point[1]]
            back_point_y = back_y[back_point[0]][back_point[1]]
            if back_point_x == start[0] and back_point_y == start[1]:
                break
            grid[back_point_x][back_point_y] -= (power // 2)
            back_point = [back_point_x, back_point_y]
            attacked_list.append(back_point)
        return
    
    else:
        dir_xx, dir_yy = [-1,-1,0,1,1,1,0,-1], [0,-1,-1,-1,0,1,1,1]
        for dxx, dyy in zip(dir_xx, dir_yy):
            pos_xx, pos_yy = end[0] + dxx, end[1] + dyy
            pos_xx, pos_yy = out_of_range(pos_xx, pos_yy)
            if grid[pos_xx][pos_yy] > 0:
                #print(end,pos_xx, pos_yy)
                grid[pos_xx][pos_yy] -= (power // 2)
                attacked_list.append([pos_xx, pos_yy])

def init():
    global attacked_list, back_x, back_y
    attacked_list = []
    back_x = [[ 0 for _ in range(m)] for __ in range(n)]
    back_y = [[ 0 for _ in range(m)] for __ in range(n)]

def check():
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0:
                count += 1
    if count == 1:
        return True
    else:
        return False

for i in range(k):  
    min_potam = select_min_potam()  
    max_potam = select_max_potam(min_potam)
    grid[min_potam[0]][min_potam[1]] += (n+m)

    attack_list[min_potam[0]][min_potam[1]] = i + 1
    bfs(min_potam, max_potam)
    for i in range(n):
        for j in range(m):
            if [i, j] not in attacked_list and grid[i][j] > 0:
                grid[i][j] += 1
            if grid[i][j] < 0:
                grid[i][j] = 0
    init()
    if check():
        break
result = -INT_MAX
for i in range(n):
    for j in range(m):
        if result < grid[i][j]:
            result = grid[i][j]
    #     print(grid[i][j], end = ' ')
    # print()
print(result)