n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
b = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if a[i][j] == b[i][j]:
            print(0,end = ' ')
        else:
            print(1,end = ' ')
    print()
