n, m = map(int,input().split())
a = []
b = []

curr = 0
for _ in range(n):
    v,t = map(int,input().split())
    for i in range(t):
        a.append(curr+v)
        curr += v

curr = 0
for _ in range(m):
    v,t = map(int,input().split())
    for i in range(t):
        b.append(curr+v)
        curr += v

result = 0
curr = ''
for i in range(len(max(a,b))):
    if a[i] > b[i] and curr != 'A':
        result += 1
        curr = 'A'
    elif a[i] < b[i] and curr != 'B':
        result += 1
        curr = 'B'
    elif a[i] == b[i] and curr != 'AB':
        result += 1
        curr = 'AB'
print(result)

# Please write your code here.