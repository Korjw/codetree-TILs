n = int(input())
arr = list(map(int, input().split()))

arr.sort()
temp = []
for i in range(n):
    temp.append(arr[i+n]-arr[i])
print(min(temp))
# Please write your code here.