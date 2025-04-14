a = list(map(int,input().split()))
for i in range(2,10):
    a.append((a[i-2]+a[i-1]) % 10)
for item in a:
    print(item,end = ' ')