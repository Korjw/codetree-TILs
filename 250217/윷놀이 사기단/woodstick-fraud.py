import sys

move_list = list(map(int, input().split()))

n = len(move_list)

first = []

for i in range(1, 21):
    first.append(i * 2)
second = [10, 13, 16, 19, 25, 30, 35, 40]
third = [20, 22, 24, 25, 30, 35, 40]
fourth = [30, 28, 27, 26, 25, 30, 35, 40]
grid = [first, second, third, fourth]

step = [[], [], [], []]
scores = [[], [], [], []]
direction = [[], [], [], []]
visited = [False for _ in range(n)]
score_sum = 0

def horse_move(j, move_list):
    global score_sum
    if len(direction[j]) > 0 and direction[j][-1][1] + move_list >= len(grid[direction[j][-1][0]]):
        scores[j].append(0)
        direction[j].append([direction[j][-1][0], 50])
        return False

    if len(scores[j]) == 0:
        scores[j].append(grid[0][move_list - 1])
        direction[j].append([0, move_list - 1])

    elif direction[j][-1][0] == 0:
        if direction[j][-1][1] + move_list < len(grid[0]):
            scores[j].append(grid[0][direction[j][-1][1] + move_list])
            direction[j].append([0, direction[j][-1][1] + move_list])
        else:
            return False

    elif direction[j][-1][0] == 1:
        if direction[j][-1][1] + move_list < len(grid[1]):
            scores[j].append(grid[1][direction[j][-1][1] + move_list])
            direction[j].append([1, direction[j][-1][1] + move_list])
        else:
            return False

    elif direction[j][-1][0] == 2:
        if direction[j][-1][1] + move_list < len(grid[2]):
            scores[j].append(grid[2][direction[j][-1][1] + move_list])
            direction[j].append([2, direction[j][-1][1] + move_list])
        else:
            return False

    elif direction[j][-1][0] == 3:
        if direction[j][-1][1] + move_list < len(grid[3]):
            scores[j].append(grid[3][direction[j][-1][1] + move_list])
            direction[j].append([3, direction[j][-1][1] + move_list])
        else:
            return False

    if scores[j][-1] == 10:
        direction[j][-1] = [1, 0]
    elif scores[j][-1] == 20:
        direction[j][-1] = [2, 0]
    elif scores[j][-1] == 30 and direction[j][-1] == [0,14]:
        direction[j][-1] = [3, 0]
    elif scores[j][-1] == 40 and direction[j][-1][1] != 50:
        direction[j][-1] = [2, 6]
    elif scores[j][-1] == 25:
        direction[j][-1] = [2, 3]

    for i in range(4):
        if len(direction[i]) > 0 and i != j and direction[j][-1][1] != 50 and (direction[i][-1] == direction[j][-1]):
            return True
    return False

count = 0
result = 0

def move(curr_idx, cnt, end):
    global count, result
    if cnt == 10 or end:
        count += 1
        if result < sum(scores[0])+sum(scores[1])+sum(scores[2])+sum(scores[3]):
            result = max(result, sum(scores[0])+sum(scores[1])+sum(scores[2])+sum(scores[3]))
            #print(result, scores, direction)
        #if (sum(scores[0])+sum(scores[1])+sum(scores[2])+sum(scores[3])) == 222:
            #print(scores, direction)
        return

    if curr_idx < n:
        for j in range(4):
            end = horse_move(j, move_list[curr_idx])
            if not end:
                move(curr_idx + 1, cnt + 1, end)
            scores[j].pop()
            direction[j].pop()


move(0, 0, False)
#print(count)
print(result)

# [[10, 30, 40, 0], [6, 16, 22, 24, 34, 40], [], []] 
# [[[1, 0], [1, 5], [2, 6], [2, 50]], 
# [[0, 2], [0, 7], [0, 10], [0, 11], [0, 16], [2, 6]], [], []]
# 5 5 2 3
# 3 5 3 1 5 3