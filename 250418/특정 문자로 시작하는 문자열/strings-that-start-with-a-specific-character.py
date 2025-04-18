n = int(input())
temp = []
for _ in range(n):
    temp.append(str(input()))
c = str(input())
n,cnt = 0, 0
for item in temp:
    if item[0] == c:
        n += len(item)
        cnt += 1

print(cnt, '{:.2f}'.format(round(n / cnt,2)))