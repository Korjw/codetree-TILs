n = int(input())
temp = list(map(int,input().split()))
temp.reverse()
for item in temp:
    if item % 2 == 0:
        print(item,end=' ')