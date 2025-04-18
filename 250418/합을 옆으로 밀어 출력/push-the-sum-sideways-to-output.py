n = int(input())
cnt = 0
for _ in range(n):
    cnt += int(input())
print(str(cnt)[1:] + str(cnt)[0])
