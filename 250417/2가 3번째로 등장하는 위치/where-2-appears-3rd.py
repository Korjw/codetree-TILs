n = int(input())
temp = list(map(int,input().split()))
cnt = 0
for i in range(len(temp)):
    if temp[i] == 2:
        cnt += 1
    if cnt == 3:
        print(i+1)
        break
