n = int(input())

out_list = []

for i in range(n):
    t,p = map(int,input().split())
    out_list.append([i,t,p])

pos = []
pos_list = []
visited = [False for _ in range(n)]

def make_pos(cnt,pos_len):
    if cnt == pos_len:
        pos_list.append(pos[:])
        return

    for i in range(n):
        if not visited[i]:
            pos.append(i)
            visited[i] = True
            make_pos(cnt+1,pos_len)
            visited[i] = False
            pos.pop()

for i in range(1,n+1):
    visited = [False for _ in range(n)]
    make_pos(0,i)

def simul(poss):
    date = [0 for _ in range(n)]
    count = 0

    for p in poss:
        start_date, t, p = out_list[p]
        for i in range(start_date,start_date+t):
            if i > n-1:
                return 0
            date[i] += 1
            if date[i] >= 2:
                return 0
        count += p
    return count

result = []
for poss in pos_list:
    result.append(simul(poss))
#print(pos_list)
print(max(result))