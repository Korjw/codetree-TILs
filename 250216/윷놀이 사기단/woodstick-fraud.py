import sys
move_list = list(map(int,input().split()))

n = len(move_list)

first = []

for i in range(1,21):
    first.append(i*2)
second = [10,13,16,19,25,30,35,40]
third = [20,22,24,25,30,35,40]
fourth = [30,28,27,26,25,30,35,40]
grid = [first, second, third, fourth]


#print(first)
step = [[],[],[],[]]
scores = [[],[],[],[]]
direction = [[],[],[],[]]
visited = [False for _ in range(n)]
score_sum = 0

def horse_move(j, move_list): # 말번호, 움직일 거리
    global score_sum
    if len(direction[j]) > 0 and direction[j][-1][1]+move_list >= len(grid[direction[j][-1][0]]):
        if scores[j][-1] == 40:
            scores[j].append(0)
        else:
            scores[j].append(40)
        direction[j].append([direction[j][-1][0], 50])
        score_sum += scores[j][-1]
        return True

    if len(scores[j]) == 0:
        scores[j].append(grid[0][move_list-1])
        direction[j].append([0,move_list-1])
        score_sum += scores[j][-1]

    elif direction[j][-1][0] == 0:
        scores[j].append(grid[0][move_list+direction[j][-1][1]])
        direction[j].append([0,direction[j][-1][1]+move_list])
        score_sum += scores[j][-1]

    elif direction[j][-1][0] == 1:
        scores[j].append(grid[1][move_list+direction[j][-1][1]])
        direction[j].append([1,direction[j][-1][1]+move_list])
        score_sum += scores[j][-1]

    elif direction[j][-1][0] == 2:
        scores[j].append(grid[2][move_list+direction[j][-1][1]])
        direction[j].append([2,direction[j][-1][1]+move_list])
        score_sum += scores[j][-1]

    elif direction[j][-1][0] == 3:
        scores[j].append(grid[3][move_list+direction[j][-1][1]])
        direction[j].append([3,direction[j][-1][1]+move_list])
        score_sum += scores[j][-1]

    if scores[j][-1] == 10:
        direction[j].pop()
        direction[j].append([1,0])
    elif scores[j][-1] == 20:
        direction[j].pop()
        direction[j].append([2,0])
    elif scores[j][-1] == 30:
        direction[j].pop()
        direction[j].append([3,0])
    
    for i in range(4):
        if len(scores[i]) > 0 and scores[i][-1] == scores[j][-1] and i != j:
            return True
    
    # 길확인 후 -> 이동 후 -> 점수추가
    # 0 이면 바로 끝(도착 뜻)
    return False

count = 0
result = 0
step_list = []

def move(curr_idx, cnt, end):
    global count, result, score_sum
    if cnt ==  10 or end:
        print(direction, scores, step)
        #step_list.append(list(map(tuple,step[:]))[:])
        count += 1
        result = max(result, score_sum)
        #print(step)
        return
    for i in range(curr_idx, n):
        for j in range(4):
            print(123,direction,scores,step)
            step[j].append(move_list[i])
            end = horse_move(j,move_list[i])
            move(i+1, cnt+1, end)
            step[j].pop()
            score_sum -= scores[j].pop()
            direction[j].pop() 

move(0,0, False)
print(count)
print(result)
#print(len(step_list))
#step_list = set(list(map(tuple,step_list)))
#print(len(step_list))