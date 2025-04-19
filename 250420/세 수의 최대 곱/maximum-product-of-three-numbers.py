import sys
n = int(input())
temp = list(map(int,input().split()))
temp.sort(key=lambda x : (-abs(x)))
result = []

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            cnt = temp[i] * temp[j]
            if cnt < 0 and temp[k] < 0:
                print(cnt*temp[k])
                sys.exit(0)
            if cnt > 0 and temp[k] > 0:
                print(cnt*temp[k])
                sys.exit(0)
            result.append(cnt*temp[k])
print(max(result))