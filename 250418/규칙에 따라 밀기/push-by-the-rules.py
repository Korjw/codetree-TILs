s = str(input())
s1 = str(input())
for i in s1:
    if i == 'L':
        s = s[1:] + s[0]
    else:
        s = s[-1] + s[:-1]
print(s)