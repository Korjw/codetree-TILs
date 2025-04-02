Q = int(input())

N, M, P = 0, 0, 0
rabbit = []
dir_x, dir_y = [-1,0,1,0], [0,-1,0,1]
score = []

def cal_xy(x,y,d,dist):
    curr_x, curr_y = x, y
    curr_dist = dist
    curr_d = d
    while curr_dist != 0:
        if curr_x+dir_x[curr_d]*curr_dist > N-1:
            #print(curr_d,curr_dist)
            curr_dist -= (N-1) - curr_x
            curr_x = N-1
            curr_d = (curr_d+2) % 4
        elif curr_x+dir_x[curr_d]*curr_dist < 0:
            #print(123,curr_x,curr_y,curr_d,curr_dist)
            curr_dist -= curr_x
            curr_x = 0
            curr_d = (curr_d+2) % 4
        elif curr_y+dir_y[curr_d]*curr_dist > M-1:
            #print(123,curr_x,curr_y,curr_d,curr_dist)
            curr_dist -= (M-1) - curr_y
            curr_y = M-1
            curr_d = (curr_d+2) % 4
            #print(123,curr_x,curr_y,curr_d,curr_dist)
        elif curr_y+dir_y[curr_d]*curr_dist < 0:
            #print(234,curr_x,curr_y,curr_d,curr_dist)
            curr_dist -= curr_y
            curr_y = 0
            curr_d = (curr_d+2) % 4
        else:
            #print(567,curr_x,curr_y,curr_d,curr_dist)
            curr_x, curr_y = curr_x+dir_x[curr_d]*curr_dist, curr_y+dir_y[curr_d]*curr_dist
            curr_dist = 0
        #print(curr_x,curr_y,curr_d,curr_dist)
    return curr_x, curr_y

def move():
    rabbit.sort(key = lambda x : (x[0], x[1]+x[2], x[1], x[2], x[3]))
    d_list = []
    for i in range(len(rabbit)):
        if i == 0:
            for k in range(4):
                curr_x, curr_y = rabbit[i][1], rabbit[i][2]
                curr_x, curr_y = cal_xy(curr_x,curr_y,k,rabbit[i][4])
                d_list.append([curr_x, curr_y])
                #break

            d_list.sort(key = lambda x : (-(x[0]+x[1]), -x[0], -x[1]))    
            rabbit[i][1], rabbit[i][2] = d_list[0][0], d_list[0][1]
            rabbit[i][0] += 1
        else:
            for k in range(len(score)):
                if score[k][0] == rabbit[i][3]:
                    score[k][1] += d_list[0][0] + d_list[0][1] + 2
        #print(score)
    #print(d_list)
    #print(rabbit)

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
            score.append([pid,0])

    if command_list[0] == 200:
        k, s = command_list[1], command_list[2]
        for _ in range(k):
            move()
        rabbit.sort(key = lambda x : (-(x[1]+x[2]), -x[1], -x[2], -x[3]))
        for k in range(len(score)):
            if score[k][0] == rabbit[0][3]:
                score[k][1] += s
    
    if command_list[0] == 300:
        pid = command_list[1]
        L = command_list[2]
        for i in range(len(rabbit)):
            if pid == rabbit[i][3]:
                rabbit[i][4] *= L

    if command_list[0] == 400:
        score.sort(key = lambda x : (-x[1]))
        print(score[0][1])


#print(score)
#print(rabbit)

