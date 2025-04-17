temp = list(map(int,input().split()))
for i in range(len(temp)):
    if temp[i] % 3 == 0:
        print(temp[i-1])
        break