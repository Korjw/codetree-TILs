X = int(input())
X -= 1
curr_v = 1
result = 1
pos = 1
for i in range(1,10000):
    #if X < 500:
        #print(curr_v,X)
    pos_curr_v = curr_v + 1
    cnt1 = 0
    cnt2 = 0
    for i in range(1,pos_curr_v+1):
        cnt1 += i
    for i in range(1,curr_v):
        cnt2 += i
    #print(cnt1,X)
    #print(cnt2,X)
    if cnt1 < X:
        curr_v = pos_curr_v
    elif curr_v == 1 or cnt2 <= X-curr_v:
        curr_v = curr_v
    else:
        curr_v -= 1
    X -= curr_v
    result += 1
    if X == 0:
        break
print(result)




# Please write your code here.