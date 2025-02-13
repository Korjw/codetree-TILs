# 커브 복제 후 끝점을 기준으로 90도 회전
# 끝점은 해당 드래곤 커브에서 시작점으로 가장 멀리 떨어진 점(그려지며 도착한 마지막 지점)

n = int(input())

dx, dy = [0,-1,0,1], [1,0,-1,0]
grid = [[[] for _ in range(101)] for __ in range(101)] # 어디랑 이어진지 적기
dragon = [] #n 차 드래곤
first, last = [0,0], [0,0] # 시작점, 끝점
rotate_grid =[[0 for _ in range(11)] for __ in range(11)]
dragon_list =[]

def out_of_range(x,y):
    return x < 0 or y < 0 or x > 10 or y > 10

def check_grid(x, y):
    global grid, rotate_grid
    for dir_x, dir_y in zip(dx,dy):
        if not out_of_range(x+dir_x, y+dir_y) and rotate_grid[x+dir_x][y+dir_y]:
            grid[x][y].append([x+dir_x, y+dir_y])

def roate(): # x, y는 끝점
    global last, rotate_grid
    diff_x, diff_y = 5 - last[0], 5 - last[1]

    for x, y in dragon:
        print(x,y,diff_x,diff_y)
        rotate_grid[x+diff_x][y+diff_y] = 1
    
    # for i in range(11):
    #     for j in range(11):
    #         print(rotate_grid[i][j], end = ' ')
    #     print()
    # print()

    rotate_grid = list(map(list, zip(*rotate_grid[::-1])))

    for i in range(11):
        for j in range(11):
            if rotate_grid[i][j]:
                rotate_grid[i][j] = 0
                rotate_grid[i-diff_x][j-diff_y] = 1
                if [i-diff_x, j-diff_y] != last:
                    print(last)
                    dragon.append([i-diff_x, j-diff_y])
    print()
    
    for i in range(11):
        for j in range(11):
            if rotate_grid[i][j]:
                check_grid(i, j)
    print()

    max_last_x, max_last_y, max_last_dist = -1, -1, -1
    for i in range(11):
        for j in range(11):
            print(rotate_grid[i][j], end = ' ')
            if rotate_grid[i][j]:
                if max_last_dist < abs(last[0]-i) + abs(last[0]-j):
                    max_last_x, max_last_y = i, j
        print()
    print()

    last[0], last[1] = max_last_x, max_last_y
    print(12345, last)

    # 돌리고
    # 돌려진 것들 중 시작점에서(first) 가장 먼거 구하기
    # 그리고 드래곤 추가
    # 그리드에 점찍기

def init():
    global rotate_grid
    rotate_grid =[[0 for _ in range(11)] for __ in range(11)]

def draw_dragon(x,y,d,g):
    for _ in range(3):
        roate()
        init()

for _ in range(1):
    x,y,d,g = map(int,input().split())
    first[0], first[1] = x, y
    last[0], last[1] = x + dx[d], y + dy[d]
    print(first,last)
    grid[first[0]][first[1]].append(last[:])
    grid[last[0]][last[1]].append(first[:])
    dragon.append(first)
    dragon.append(last[:])
    draw_dragon(x,y,d,g)
    # dragon_list 추가 grid에서 이어졌는지 체크 ex. [i+1, j], [i, j+1]
    # i,j i+1,j+1 까지 4개 조가

print(dragon)

for i in range(11):
    for j in range(11):
        print(grid[i][j], end = ' ')
    print()