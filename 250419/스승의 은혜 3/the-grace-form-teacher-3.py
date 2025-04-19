n,b = map(int,input().split())
ps = []
result = 0

for _ in range(n):
    p,s = map(int,input().split())
    ps.append([p,s])

for i in range(n):
    temp = ps[:][:]
    temp[i][0] //= 2
    temp.sort(key = lambda x : (x[0]+x[1]))
    #print(ps,temp)
    cnt = 0
    count = 0
    for j in range(n):
        cnt += (temp[j][0] + temp[j][1])
        if cnt <= b:
            count += 1
            result = max(result,count)
        else:
            break
print(result)