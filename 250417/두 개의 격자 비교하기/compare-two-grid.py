n,m = map(int,input().split())
temp = [list(map(int,input().split())) for _ in range(n)]
temp2 = [list(map(int,input().split())) for _ in range(n)]
temp3 = [[0 for _ in range(m)] for __ in range(n)]

for i in range(n):
    for j in range(m):
        if temp[i][j] != temp2[i][j]:
            temp3[i][j] = 1
        print(temp3[i][j],end = ' ')
    print()