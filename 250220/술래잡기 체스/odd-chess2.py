grid =[[[] for _ in range(4)] for __ in range(4)]
grid_list = []
horse_list = []
dx, dy = [-1,-1,0,1,1,1,0,-1], [0,-1,-1,-1,0,1,1,1]

for i in range(4):
    p1,d1,p2,d2,p3,d3,p4,d4 = list(map(int,input().split()))
    grid[i][0] = [p1,d1-1]
    grid[i][1] = [p2,d2-1]
    grid[i][2] = [p3,d3-1]
    grid[i][3] = [p4,d4-1]
    horse_list.append([i,0,p1,d1-1])
    horse_list.append([i,1,p2,d2-1])
    horse_list.append([i,2,p3,d3-1])
    horse_list.append([i,3,p4,d4-1])

sulrae = [[0,0,grid[0][0][1]]] # x 위치, y 위치, 방향
horse_list.remove([0,0,grid[0][0][0],grid[0][0][1]])
score = [[0,0,grid[0][0][0],grid[0][0][1]]]
grid[0][0] = [-1,-1]
total_count = 0
grid_list.append(grid[:])

for i in range(4):
    for j in range(4):
        print(grid[i][j], end = ' ')
    print()

def out_of_range(x,y):
    return x < 0 or y < 0 or x > 3 or y > 3

total_count = 0

def horse_move():
    check_grid = grid_list[-1]
    next_grid  = grid_list[-1][:]

    horse_list.sort(lambda key = x : x[2])

    for i in range(len(horse_list)):
        x, y, d = horse_list[i][0], horse_list[i][1], horse_list[i][3]
        for k in range(8):
            d = (d+1) % 8
            x, y = x+dx[d], y+dy[d]
            if not out_of_range(x, y) and [x,y] != [sulrae[-1][0], sulrae[-1][1]]:
                # 위치를 바꿈
                # next_grid에 표시

def sulrae_move(end):
    global total_count
    if end:
        #print(564, sulrae, score)
        return
    print(end, sulrae)
    count = 0
    for i in range(1,4):
        curr_x, curr_y, direction = sulrae[-1][0], sulrae[-1][1], sulrae[-1][2]
        x, y = curr_x+dx[direction]*i, curr_y+dy[direction]*i
        if not out_of_range(x,y):
            count += 1
            number = grid[x][y][0]
            
            # 말이동
            # horse_move(grid_list.append)
            # horse_list 현재 grid 기준으로 만들기 
            # 술래잡기
            sulrae.append([x,y,direction])
            score.append([x,y,grid[x][y][0],grid[x][y][1]])
            horse_list.remove([x,y,grid[x][y][0],grid[x][y][1]])
            grid[x][y] = [-1,-1]

            move(end)

            # grid_list pop
            # horse_list 현재 grid 기준으로 만들기 
            score.pop()
            sulrae.pop()
            grid[x][y] = [number, direction]
            horse_list.append([x,y,number,direction])

    # total_count += 1   
    # if total_count:     
    #     print(5435, count)
    #     end = True
    if count == 0:
        end = True

horse_move()
sulrae_move(False)

print(sulrae)
horse_list.sort(key = lambda x : -x[2])

for i in range(4):
    for j in range(4):
        print(grid[i][j], end = ' ')
    print()

print(len(score))
print(score)
print(len(horse_list))
print(horse_list)

