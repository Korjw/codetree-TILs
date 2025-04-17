temp = list(map(int,input().split()))

for i in range(2,10):
    temp.append(temp[i-1] + 2 * temp[i-2])
for item in temp:
    print(item,end = ' ')