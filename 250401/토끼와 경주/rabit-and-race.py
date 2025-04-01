Q = int(input())

N, M, P = 0, 0, 0
rabbit = []
dir_x, dir_y = [-1,1,0,0], [0,0,-1,1]

def out_of_range(x,y):
    if x < 0:
        return x+N+1, y
    if x > N -1:
        return x-N-1, y
    if y < 0:
        return x, y+M+1
    if y > M-1:
        return x, y-M-1
    return x, y

def move():
    rabbit.sort(key = lambda x : (x[0], x[1]+x[2], x[1], x[2], x[3]))
    for i in range(len(rabbit)):
        d_list = []
        for dx, dy in zip(dir_x, dir_y):
            curr_x, curr_y = rabbit[i][1], rabbit[i][2]
            for _ in range(rabbit[i][4]):
                curr_x, curr_y = out_of_range(curr_x + dx, curr_y + dy)
            d_list.append([curr_x, curr_y])
        print(d_list)
    return

for _ in range(Q):
    command_list = list(map(int,input().split()))
    if command_list[0] == 100:
        N = command_list[1]
        M = command_list[2]
        P = command_list[3]
        cnt = 4
        for i in range(P):
            pid = command_list[cnt]
            cnt += 1
            d = command_list[cnt]
            cnt += 1
            rabbit.append([0,0,0,pid,d]) # 점프횟수, 행, 열, 고유번호, 만큼이동하는 거리

    if command_list[0] == 200:
        k, s = command_list[1], command_list[2]
        for _ in range(k):
            move()
            break



print(rabbit)
