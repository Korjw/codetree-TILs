a,b = map(int,input().split())
cnt = 1
for i in range(1,b+1):
    if i % a == 0:
        cnt *= i
print(cnt)