N, S = map(int, input().split())
arr = list(map(int, input().split()))

pos_list = []
pos = []
result = 999999999

def make_pos(x,cnt):
    if x == 2:
        pos_list.append(pos[:])
        return
    for i in range(cnt,N):
        pos.append(i)
        make_pos(x+1,i+1)
        pos.pop()

make_pos(0,0)
#print(pos_list)

def simul():
    global result
    for p in pos_list:
        temp = arr[:]
        temp.remove(arr[p[0]])
        temp.remove(arr[p[1]])
        result = min(result,abs(S-sum(temp)))

simul()
print(result)
# Please write your code here.