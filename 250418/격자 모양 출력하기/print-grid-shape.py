n,m = map(int,input().split())
temp = [[0 for _ in range(n)] for __ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    temp[a-1][b-1] = a*b
for i in range(n):
    for j in range(n):
        print(temp[i][j],end = ' ')
    print()
