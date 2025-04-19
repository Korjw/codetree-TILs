n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
result = 99999999
for i in range(n):
    temp = [[] for _ in range(102)]
    for j in range(n):
        if i == j:
            continue
        x1,x2 = segments[j][0], segments[j][1]
        for k in range(x1,x2+1):
            temp[k].append(j)
    #print(temp)
    cnt = 0
    for j in range(102):
        if len(temp[j]):
            cnt = j 
            break
    for j in range(101,-1,-1):
        if len(temp[j]):
            cnt = j - cnt
            break
    result = min(result,cnt)
print(result)
# Please write your code here.