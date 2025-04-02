Q = int(input())

N, M, P = 0, 0, 0
rabbit = []
dir_x, dir_y = [-1,0,1,0], [0,-1,0,1]
score = []

def out_of_range(x,y,d):
    if x < 0 or x > N -1 or y < 0 or y > M-1:
        return (d+2) % 4
    return d

def move():
    rabbit.sort(key = lambda x : (x[0], x[1]+x[2], x[1], x[2], x[3]))
    d_list = []
    for i in range(len(rabbit)):
        if i == 0:
            for k in range(4):
                curr_d = k
                curr_x, curr_y = rabbit[i][1], rabbit[i][2]
                for _ in range(rabbit[i][4]):
                    curr_d = out_of_range(curr_x + dir_x[curr_d], curr_y + dir_y[curr_d],curr_d)
                    curr_x, curr_y = curr_x + dir_x[curr_d], curr_y + dir_y[curr_d]
                d_list.append([curr_x, curr_y])

            d_list.sort(key = lambda x : (-(x[0]+x[1]), -x[0], -x[1]))    
            rabbit[i][1], rabbit[i][2] = d_list[0][0], d_list[0][1]
            rabbit[i][0] += 1
        else:
            for k in range(len(score)):
                if score[k][0] == rabbit[i][3]:
                    score[k][1] += d_list[0][0] + d_list[0][1] + 2
        #print(score)
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

