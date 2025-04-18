n = int(input())
arr = list(map(int, input().split()))

def func(x):
    cnt = 0
    for i in arr:
        if x % i == 0:
            cnt += 1
    if cnt == len(arr):
        print(x)
        return
    func(x+1)
func(max(arr))
# Please write your code here.