import sys
n = int(input())
arr = list(map(int, input().split()))

def func(x):
    cnt = 0
    for i in arr:
        if x % i == 0:
            cnt += 1
        else:    
            func(x+1)
    if cnt == len(arr):
        print(x)
        sys.exit(0)
func(max(arr))
# Please write your code here.