a,b = map(int,input().split())
temp = [0 for _ in range(b+1)]
while a > 1:
    temp[a % b] += 1
    a //= b

cnt = 0
for item in temp:
    cnt += item * item
print(cnt)