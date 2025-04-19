n, k = map(int, input().split())
arr = list(map(int, input().split()))

result = 9999999999
max_num, min_num = max(arr),min(arr)
for i in range(min_num, max_num+1): # 최소값
    cnt = 0
    for s in arr:
        if s < i:
            cnt += abs(s-i)
        if s > i + k:
            cnt += abs(s-i-k)
    result = min(result,cnt)
print(result) 
# Please write your code here.