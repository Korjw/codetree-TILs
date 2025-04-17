n = int(input())
cnt = 0
for _ in range(n):
    a = int(input())
    if a % 2 == 1 and a % 3 == 0:
        cnt += a
print(cnt)