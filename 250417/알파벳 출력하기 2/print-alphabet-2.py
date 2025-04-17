n = int(input())
string = 'A'
for i in range(n,0,-1):
    for _ in range(n-i):
        print(' ',end = ' ')
    for _ in range(i):
        print(string, end = ' ')
        string = chr(ord(string) + 1)
        if string == '[':
            string = 'A'
    print()
