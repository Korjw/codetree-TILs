n, L = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(n)]
slip_grid =[[0 for _ in range(n)] for __ in range(n)] # 보도블럭 세로
slip_grid2 =[[0 for _ in range(n)] for __ in range(n)] # 보도블럭 가로
# L길이가 2라면 최소 3개 체크
# n 6 L 2 n-L-1 3

def out_of_range(x,y):
    return x < 0 or y < 0 or x > n-1 or y > n-1

def check_heng(y):
    for i in range(n-L): # 0 ~ 3 아래로 체크 직각이 아래
        block_first_height = grid[i][y]
        block_last_height  = grid[i+L][y]
        length_count = 0
        for k in range(i,i+L): # 0, 1
            if grid[k][y] == block_first_height:
                length_count += 1
            else:
                continue

        if length_count == L and block_last_height - block_first_height == 1:
            slip_grid[i+L][y] = 1

    for i in range(n-1,L-1,-1): # 5 ~ 2 위로 체크 직각이 위
        block_first_height = grid[i][y]
        block_last_height  = grid[i-L][y]
        length_count = 0
        for k in range(i,i-L,-1): # 5, 4
            if grid[k][y] == block_first_height:
                length_count += 1
            else:
                continue

        if length_count == L and block_last_height - block_first_height == 1:
            count = 0
            for o in range(L*2):
                if not out_of_range(i-L+1+o, y) and slip_grid[i-L+1+o][y] == 1:
                    slip_grid[i-L+1+o][y] = 0
                    count += 1
            if count == 0:
                slip_grid[i-L][y] = 2

    

def check_yeol(x): # 오른쪽 왼쪽 체크
    for j in range(n-L): # 0 ~ 3 오른쪽 체크 직각이 오른쪽
        block_first_height = grid[x][j]
        block_last_height  = grid[x][j+L]
        length_count = 0
        for l in range(j,j+L): # 0, 1
            if grid[x][l] == block_first_height:
                length_count += 1
            else:
                continue

        if length_count == L and block_last_height - block_first_height == 1:
            slip_grid2[x][j+L] = 1

    for j in range(n-1,L-1,-1): # 5 ~ 2 직각이 왼쪽
        block_first_height = grid[x][j]
        block_last_height  = grid[x][j-L]
        length_count = 0
        for l in range(j,j-L,-1): # 5, 4
            if grid[x][l] == block_first_height:
                length_count += 1
            else:
                continue

        if length_count == L and block_last_height - block_first_height == 1:
            count = 0
            for p in range(L*2): # 범위 더 넓게 체크
                if not out_of_range(x, j-L+1+p) and slip_grid2[x][j-L+1+p] == 1:
                    slip_grid2[x][j-L+1+p] = 0
                    count += 1
            if count == 0:
                slip_grid2[x][j-L] = 2
    
result = 0

def check():
    global result
    for i in range(n):
        check_num = grid[i][0]
        check_count = True
        for j in range(1,n):
            #print(i, j, check_num, grid[i][j], slip_grid2[i][j])
            if grid[i][j] > check_num and slip_grid2[i][j] == 1:
                check_num = grid[i][j]
            
            elif grid[i][j] < check_num and slip_grid2[i][j-1] == 2:
                check_num = grid[i][j]
            
            elif grid[i][j] == check_num:
                continue
            
            else:
                check_count = False
                break
        if check_count:
            #print(i)
            result += 1
    
    for i in range(n):
        check_num = grid[0][i]
        check_count = True
        for j in range(1,n):
            #print(j, i, check_num, grid[j][i], slip_grid[j][i], slip_grid[j-1][i])
            if grid[j][i] > check_num and slip_grid[j][i] == 1:
                check_num = grid[j][i]
            
            elif grid[j][i] < check_num and slip_grid[j-1][i] == 2:
                check_num = grid[j][i]
            
            elif grid[j][i] == check_num:
                continue
            
            else:
                check_count = False
                break
        if check_count:
            #print(i)
            result += 1
        


for i in range(n):
    check_heng(i)
    check_yeol(i)

check()

# for i in range(n):
#     for j in range(n):
#         print(slip_grid[i][j], end = ' ')
#     print()

# print()

# for i in range(n):
#     for j in range(n):
#         print(slip_grid2[i][j], end = ' ')
#     print()
print(result)
