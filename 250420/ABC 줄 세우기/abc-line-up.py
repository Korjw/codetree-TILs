n = int(input())
arr = list(input().split())

result = 0

def move(i):
    global result
    while ord(arr[i])-ord('A') != i:
        temp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = temp
        i += 1
        result += 1

for i in range(n):
    if ord(arr[i])-ord('A') != i:
        move(i)
        
print(result)