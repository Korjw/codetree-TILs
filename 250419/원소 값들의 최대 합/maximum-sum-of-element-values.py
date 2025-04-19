n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

result = 0

for i in range(1,n+1):
    temp = arr[:]
    cnt = 0
    curr = i
    sum_num = 0
    for j in range(m):
        if j == 0:
            if temp[curr] != curr:
                #print(i,curr,temp[curr],temp)
                cnt += 1
                sum_num += temp[curr]
                #curr = arr[curr]
                temp2 = temp[curr] # 5 
                temp3 = temp[temp2] # 3
                temp[temp2] = temp2
                curr = temp3
                #print(i,curr,temp[curr],temp2,temp3,temp)
        else:
            if temp[curr] != curr:
                #print(i,curr,temp[curr],temp)
                cnt += 1
                sum_num += curr
                #curr = arr[curr]
                temp2 = temp[curr] # 4
                temp[curr] = curr
                curr = temp2
                #print(i,curr,temp[curr],temp2,temp3,temp)

    if cnt == m:
        #print(i,sum_num)
        result = max(result,sum_num)
print(result)