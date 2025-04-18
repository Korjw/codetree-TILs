s = str(input())
cnt = 0
for i in s:
    if i <= '9' and i >= '0':
        cnt += int(i)
print(cnt)