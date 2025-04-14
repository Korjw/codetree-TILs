n = int(input())
a = [[0 for _ in range(n)] for __ in range(n)]

for j in range(n):
    if j % 2 == 0:
        for i in range(n):
            a[i][j] = i+1
    else:
        for i in range(n-1,-1,-1):
            a[i][j] = n - i

for i in range(n):
    for j in range(n):
        print(a[i][j],end = '')
    print()