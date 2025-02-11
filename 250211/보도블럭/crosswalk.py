n, L = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(n)]
slip_grid =[[0 for _ in range(n)] for __ in range(n)]
# L길이가 2라면 최소 3개 체크
# n 6 L 2 n-L-1 3
def check_heng(y):
    for i in range(n-L): # 0 ~ 3 아래로 체크 직각이 아래
        block_first_height = grid[i][y]
        block_last_height  = grid[i+2][y]
        length_count = 0
        for k in range(i,i+L): # 0, 1
            if grid[k][y] == block_first_height:
                length_count += 1
            else:
                continue

        if length_count == L and block_last_height - block_first_height == 1:
            slip_grid[i+2][y] = 1

    for i in range(n-1,L-1,-1): # 5 ~ 2 위로 체크 직각이 위
        block_first_height = grid[i][y]
        block_last_height  = grid[i-2][y]
        length_count = 0
        for k in range(i,i-L,-1): # 5, 4
            if grid[k][y] == block_first_height:
                length_count += 1
            else:
                continue

        if length_count == L and block_last_height - block_first_height == 1:
            count = 0
            for o in range(L):
                if slip_grid[i-1+o][y] == 1:
                    slip_grid[i-1+o][y] = 0
                    count += 1
            if count == 0:
                slip_grid[i-2][y] = 1

    

def check_yeol(x): # 오른쪽 왼쪽 체크
    for j in range(n-L): # 0 ~ 3 오른쪽 체크 직각이 오른쪽
        block_first_height = grid[x][j]
        block_last_height  = grid[x][j+2]
        length_count = 0
        for l in range(j,j+L): # 0, 1
            if grid[x][l] == block_first_height:
                length_count += 1
            else:
                continue

        if length_count == L and block_last_height - block_first_height == 1:
            slip_grid[x][j+2] = 1

    for j in range(n-1,L-1,-1): # 5 ~ 2 직각이 왼쪽
        block_first_height = grid[x][j]
        block_last_height  = grid[x][j-2]
        length_count = 0
        for l in range(j,j-L,-1): # 5, 4
            if grid[x][l] == block_first_height:
                length_count += 1
            else:
                continue

        if length_count == L and block_last_height - block_first_height == 1:
            count = 0
            for p in range(L):
                if slip_grid[x][j-1+p] == 1:
                    slip_grid[x][j-1+p] = 0
                    count += 1
            if count == 0:
                slip_grid[x][j-2] = 1
    

result = 0

for i in range(n):
    if check_heng(i):
        print(1,i)
        result += 1
    if check_yeol(i):
        print(2,i)
        result += 1

for i in range(n):
    for j in range(n):
        print(slip_grid[i][j], end = ' ')
    print()
print(result)
