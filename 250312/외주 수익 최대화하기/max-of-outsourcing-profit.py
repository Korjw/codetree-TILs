n = int(input())

out_list = []

for i in range(n):
    t,p = map(int,input().split())
    out_list.append([i,t,p])

pos = []
pos_check = [0]
pos_list = []
visited = [False for _ in range(n)]
result = [0]

def make_pos(cnt,pos_len):
    global result
    if cnt == pos_len:
        pos_list.append(pos[:])
        return

    for i in range(n):
        if not visited[i] and pos_check[-1]-1 + out_list[i][1] <= n-1 and pos_check[-1]-1 < out_list[i][0] and \
            out_list[i][0] + out_list[i][1] <= n:
            pos.append(i)
            pos_check.append(out_list[i][0] + out_list[i][1])
            visited[i] = True
            make_pos(cnt+1,pos_len)
            visited[i] = False
            pos.pop()
            pos_check.pop()

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

for i in range(1,n+1):
    pos = []
    pos_check = [0]
    pos_list = []
    visited = [False for _ in range(n)]
    make_pos(0,i)
    for poss in pos_list:
        result.append(simul(poss))
#print(pos_list)
print(max(result))