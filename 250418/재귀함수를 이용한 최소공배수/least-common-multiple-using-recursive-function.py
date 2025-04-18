import sys
n = int(input())
arr = list(map(int, input().split()))
result = 1
def func(s1,s2,x):
    global result
    cnt = 0
    for i in range(s1,s2+1):
        if x % arr[i] == 0:
            cnt += 1
    if cnt == 2:
        result = x
        return
    else:
        func(s1,s2,x+result)
for i in range(len(arr)-1):
    func(i,i+1,result)
if len(arr) == 1:
    result = arr[0]
print(result)
# Please write your code here.