n = int(input())
cnt = 1
for i in range(n):
    for j in range(n*cnt,0,-1 * cnt):
        print(j, end = ' ')
    cnt += 1
    print()
