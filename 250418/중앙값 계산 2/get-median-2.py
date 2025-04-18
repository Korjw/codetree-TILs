n = int(input())
arr = list(map(int, input().split()))

temp = []
for i in range(n):
    temp.append(arr[i])
    if i % 2 == 0:
        temp.sort()
        print(temp[len(temp) // 2],end = ' ')
# Please write your code here.