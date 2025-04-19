n,h,t = map(int, input().split())
arr = list(map(int, input().split()))

result = 999999999
for i in range(n-t):
    cnt = 0
    for j in range(i,i+t):
        cnt += abs(arr[j]-h)
    result = min(result,cnt)
print(result)