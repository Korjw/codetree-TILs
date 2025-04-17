n = int(input())
temp = [[0 for _ in range(n)]for __ in range(n)]

cnt = 1
tf = 0
for j in range(n-1,-1,-1):
    if tf % 2 == 0:
        for i in range(n-1,-1,-1):
            temp[i][j] = cnt
            cnt += 1
    else:
        for i in range(n):
            temp[i][j] = cnt
            cnt += 1
    tf += 1

for i in range(n):
    for j in range(n):
        print(temp[i][j],end = ' ')
    print()
        