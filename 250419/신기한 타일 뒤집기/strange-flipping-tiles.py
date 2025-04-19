n = int(input())
temp = [0 for _ in range(999999)]
curr = 103


for _ in range(n):
    x, c = map(str,input().split())
    x = int(x)
    #print(curr)
    if c == 'L':
        for i in range(curr-x+1,curr+1):
            if temp[i] != 3:
                temp[i] = 1
        curr = curr-x+1
    else:
        for i in range(curr,curr+x):
            if temp[i] != 3:
                temp[i] = 2
        curr = curr+x-1

print(temp.count(1),temp.count(2))
