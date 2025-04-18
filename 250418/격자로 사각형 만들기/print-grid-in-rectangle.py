n = int(input())
temp = [[ 0 for _ in range(n)] for __ in range(n)]
for i in range(n):
    temp[i][0] = 1
    temp[0][i] = 1

for i in range(1,n):
    for j in range(1,n):
        temp[i][j] = temp[i-1][j] + temp[i][j-1] + temp[i-1][j-1]

for i in range(n):
    for j in range(n):
        print(temp[i][j],end = ' ')
    print()
