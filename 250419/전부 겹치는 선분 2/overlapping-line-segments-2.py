n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
temp = [0 for _ in range(101)]
tf = False
for i in range(n):
    temp = [[] for _ in range(101)]
    for j in range(n):
        if i == j:
            continue
        else:
            x1,x2 = segments[j][0], segments[j][1]
            for k in range(x1,x2+1):
                temp[k].append(j)
    #print(temp)
    temp2 = []
    for item in temp:
        if len(item) == n-1:
            tf = True
            break
    if tf:
        break
if tf:
    print('Yes')
else:
    print('No')

# Please write your code here.