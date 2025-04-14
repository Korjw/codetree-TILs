cnt = 0
cnt1 = 0
for _ in range(10):
    a = int(input())
    if a % 3 == 0:
        cnt += 1
    if a % 5 == 0:
        cnt1 += 1

print(cnt,cnt1)