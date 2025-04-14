a =int(input())
cnt = 0

for i in range(1,a+1):
    if i % 2 and i % 3 and i % 5:
        cnt +=1

print(cnt)