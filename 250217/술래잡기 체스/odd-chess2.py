grid =[[[] for _ in range(4)] for __ in range(4)]
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

sulrae = [0,0,grid[0][0][1]] # x 위치, y 위치, 방향
horse_list.remove([0,0,grid[0][0][0],grid[0][0][1]])
grid[0][0] = [-1,-1]
score = [grid[0][0][0]]

for i in range(4):
    for j in range(4):
        print(grid[i][j], end = ' ')
    print()

def move(end):
    if end:
        return
    while True:
        curr_x, curr_y, direction = sulrae[0], sulrae[1], sulrae[2]
        count = 0
        for i in range(4):
            return
        if count != 0:
            move(end)
        else:
            end = True

    return
move(False)

print(sulrae)
horse_list.sort(key = lambda x : -x[2])
print(horse_list)