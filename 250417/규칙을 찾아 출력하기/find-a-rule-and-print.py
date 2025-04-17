n = int(input())
for _ in range(n):
    print('*', end = ' ')
print()
for i in range(1,n):
    for _ in range(i):
        print('*',end = ' ')
    for _ in range(n-i-1):
        print(' ',end = ' ')
    print('*',end = ' ')
    print()