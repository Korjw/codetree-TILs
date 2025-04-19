X, Y = map(int, input().split())
cnt = 0

for i in range(X,Y+1):
    temp = str(i)
    n = len(temp)
    tf = True
    for j in range(n//2):
        if temp[j] != temp[n-1-j]:
            tf = False
    if tf:
        cnt += 1

print(cnt)