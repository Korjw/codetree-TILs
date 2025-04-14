a = int(input())
cnt = 0
for i in range(1, 5000):
    cnt += i
    if cnt >= a:
        print(i)
        break