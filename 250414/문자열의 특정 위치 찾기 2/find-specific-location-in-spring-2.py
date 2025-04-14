string = ["apple","banana","grape","blueberry","orange"]
a = input()
b = []
cnt = 0
for item in string:
    if item[2] == a or item[3] == a:
        b.append(item)

for s in b:
    print(s)
print(len(b))