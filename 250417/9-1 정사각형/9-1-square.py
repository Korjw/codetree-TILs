n = int(input())
cnt = 9
pn = False
temp = [[0 for _ in range(n)]for __ in range(n)]
for i in range(n):
    for j in range(n):
        temp[i][j] = cnt
        cnt -= 1
        if cnt == 0:
            cnt = 9
    

for i in range(n):
    for j in range(n):
        print(temp[i][j],end = '')
    print()
