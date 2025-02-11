n, L = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(n)]

# L길이가 2라면 최소 3개 체크
# n 6 L 2 n-L-1 3
def check_heng(y):
    for i in range(n-L): # 0 ~ 3 아래로 체크
        block_first_height = grid[i][y]
        block_last_height  = grid[i+2][y]
        length_count = 0
        for k in range(i,i+L): # 0, 1
            if grid[k][y] == block_first_height:
                length_count += 1
            else:
                continue

        if length_count == L and block_last_height - block_first_height == 1:
            print(1,y,i)

    for i in range(n-1,L-1,-1): # 5 ~ 2 위로 체크
        block_first_height = grid[i][y]
        block_last_height  = grid[i-2][y]
        length_count = 0
        for k in range(i,i-L,-1): # 5, 4
            if grid[k][y] == block_first_height:
                length_count += 1
            else:
                continue

        if length_count == L and block_last_height - block_first_height == 1:
            print(2,y,i)

def check_yeol(x): # 오른쪽 왼쪽 체크
    return

#for i in range(n):
check_heng(0)