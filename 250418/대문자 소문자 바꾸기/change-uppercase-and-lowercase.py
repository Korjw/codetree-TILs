s = str(input())
for i in s:
    if i <= 'Z' and i >= 'A':
        print(i.lower(),end = '')
    else:
        print(i.upper(), end = '')