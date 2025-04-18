m1, d1, m2, d2 = map(int, input().split())
cnt = 0
for i in range(1,m1):
    if i in [1,3,5,7,8,10,12]:
        cnt += 31
    elif i == 2:
        cnt += 29
    else:
        cnt += 30
cnt += d1 
cnt2 = 0
for i in range(1,m2):
    if i in [1,3,5,7,8,10,12]:
        cnt2 += 31
    elif i == 2:
        cnt2 += 29
    else:
        cnt2 += 30
cnt2 += d2 
A = input()
#print(cnt2,cnt)
if A == 'Tue':
    cnt += 1
if A == 'Wed':
    cnt += 2
if A == 'Thu':
    cnt += 3
if A == 'Fri':
    cnt += 4
if A == 'Sat':
    cnt += 5
if A == 'Sun':
    cnt += 6

print((cnt2-cnt)// 7+1)
# Please write your code here.