n = int(input())

grid = [[-1 for _ in range(202)] for __ in range(202)]

cnt = 1
for _ in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    x1,y1,x2,y2 = x1 + 101, y1 + 101, x2 + 101, y2 + 101
    for i in range(x1,x2):
        for j in range(y1,y2):
            grid[i][j] = cnt % 2
    cnt += 1
result = 0
for i in range(202):
    for j in range(202):
        if grid[i][j] == 0:
            result += 1
print(result)
