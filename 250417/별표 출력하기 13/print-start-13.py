n = int(input())
a = n
b = 1
for i in range(n//2):
    a -= i
    b += i
    for _ in range(a):
        print('*', end = ' ')
    print()
    for _ in range(b):
        print('*', end = ' ')
    print()
if n % 2 == 1:
    a -= 1
    for _ in range(a):
        print('*', end = ' ')
    print()

    for _ in range(a):
        print('*', end = ' ')
    print()

a = 1
b = n
for i in range(n//2):
    a += i
    b -= i
    for _ in range(a):
        print('*', end = ' ')
    print()
    for _ in range(b):
        print('*', end = ' ')
    print()
