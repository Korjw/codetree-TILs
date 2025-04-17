n = int(input())
a = n
b = 1
for i in range(n//2):
    for _ in range(a):
        print('*', end = ' ')
    print()
    for _ in range(b):
        print('*', end = ' ')
    print()
    a -= 1
    b += 1

if n % 2 == 1:
    for _ in range(a):
        print('*', end = ' ')
    print()

    for _ in range(a):
        print('*', end = ' ')
    print()

a += 1
b -= 1
for i in range(n//2):
    for _ in range(b):
        print('*', end = ' ')
    print()
    for _ in range(a):
        print('*', end = ' ')
    print()
    a += 1
    b -= 1
