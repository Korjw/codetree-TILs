n = int(input())
temp = list(map(int,input().split()))

cnt = 99999999
for i in range(1,len(temp)):
    if temp[i] - temp[i-1] < cnt:
        cnt = temp[i] - temp[i-1]

print(cnt)