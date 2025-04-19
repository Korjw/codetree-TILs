X = int(input())

pos = []
curr = 1
result = 0

for i in range(1,200):
    cnt = 0
    for j in range(1,i+1):
        cnt += j
    for j in range(1,i):
        cnt += j
    pos.append(cnt)
for i in range(200):
    if pos[i] <= X and pos[i+1] > X:
        X -= pos[i]
        result = i * 2 + 1
        break
print(result+X)
# Please write your code here.