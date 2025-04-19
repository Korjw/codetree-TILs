n = int(input())
temp = [0 for _ in range(999999)]
curr = 103

b = [0 for _ in range(999999)]
w = [0 for _ in range(999999)]

for _ in range(n):
    x, c = map(str,input().split())
    x = int(x)
    #print(curr)
    if c == 'L':
        for i in range(curr-x+1,curr+1):
            if temp[i] != 3:
                temp[i] = 1
                w[i] += 1
            if b[i] >= 2 and w[i] >= 2:
                temp[i] = 3
        curr = curr-x+1
    else:
        for i in range(curr,curr+x):
            if temp[i] != 3:
                temp[i] = 2
                b[i] += 1
            if b[i] >= 2 and w[i] >= 2:
                temp[i] = 3
        curr = curr+x-1

print(temp.count(1),temp.count(2),temp.count(3))
