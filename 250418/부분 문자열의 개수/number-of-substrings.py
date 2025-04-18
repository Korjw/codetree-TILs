a = str(input())
b = str(input())
result = 0

for i in range(len(a)):
    cnt = 0
    for j in range(i,i+len(b)):
        if j >= len(a):
            break
        if b[j-i] == a[j]:
            cnt += 1
    if cnt == len(b):
        result += 1

print(result)