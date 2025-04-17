n = int(input())
for i in range(1,n+1):
    cnt = i
    for _ in range(i):
        print(cnt,end = ' ')
        cnt += i
    print()