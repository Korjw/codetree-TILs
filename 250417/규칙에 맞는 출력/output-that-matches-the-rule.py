n = int(input())
for i in range(1,n+1):
    cnt = n+1-i
    for _ in range(i):
        print(cnt,end = ' ')
        cnt += 1
    print()