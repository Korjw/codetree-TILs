a  = str(input())
s1 = a[0]
s2 = a[1]
b = ""
for item in a:
    if item == s1:
        b += s2
    elif item == s2:
        b += s1
    else:
        b += item
print(b)