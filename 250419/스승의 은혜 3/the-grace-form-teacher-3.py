n,b = map(int,input().split())
ps = []
result = 0

for _ in range(n):
    p,s = map(int,input().split())
    ps.append([p,s])
ps.sort()
for i in range(n):
    cnt = 0
    count = 0
    for j in range(n):
        if j == i:
            cnt += (ps[i][0] // 2 + ps[i][1])
        else:
            cnt += (ps[j][0] + ps[j][1])
        if cnt <= b:
            count += 1
            result = max(result,count)
        else:
            break
print(result)