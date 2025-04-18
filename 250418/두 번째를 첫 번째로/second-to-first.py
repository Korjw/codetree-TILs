s = str(input())
s2 = s[1]
s1 = s[0]
b = ""
for item in s:
    if item == s2:
        b += s1
    else:
        b += item
print(b)