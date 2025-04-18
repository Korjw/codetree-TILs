s1 = str(input())
s2 = str(input())

s3, s4 = "", ""
for i in s1:
    if i >= '0' and i <= '9':
        s3 += i
for i in s2:
    if i >= '0' and i <= '9':
        s4 += i

print(int(s3)+int(s4))