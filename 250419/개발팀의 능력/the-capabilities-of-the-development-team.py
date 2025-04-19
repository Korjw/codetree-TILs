arr = list(map(int, input().split()))
n = 5
result = 999999999
for i in range(n):
    for j in range(i+1,n):
        cnt1 = arr[i]+arr[j]
        for k in range(n):
            if i != k and j != k:
                cnt2 = arr[k]
                if [(sum(arr)-cnt1-cnt2),cnt1,cnt2].count(cnt1) >= 2 or [(sum(arr)-cnt1-cnt2),cnt1,cnt2].count(cnt2) >= 2:
                    continue
                result = min(result, max([(sum(arr)-cnt1-cnt2),cnt1,cnt2])-min([(sum(arr)-cnt1-cnt2),cnt1,cnt2]))  
if result == 999999999:
    print(-1)
else:      
    print(result)
