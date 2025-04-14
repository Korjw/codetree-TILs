a = int(input())
cnt = 1
for i in range(1,a+1):
    for _ in range(i):
        print(cnt, end = ' ')
        cnt += 1
    print()