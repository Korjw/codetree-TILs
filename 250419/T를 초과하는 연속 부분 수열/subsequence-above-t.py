n, t = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
max_num = -1
cnt = 0
for i in arr:
    #print(i,max_num,cnt)
    if t < i:
        max_num = i
        cnt += 1
    else:
        if cnt >= 1:
            result = max(result,cnt)
        cnt = 0
        max_num = i
print(result)
# Please write your code here.