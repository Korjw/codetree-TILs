n = int(input())
arr = list(input().split())

result = 0

def move1(i,curr):
    global result
    x = curr
    while x != i:
        temp = arr[x]
        arr[x] = arr[x+1]
        arr[x+1] = temp
        x += 1
        result += 1
        

def move2(i,curr):
    global result
    x = curr
    while x != i:
        temp = arr[x-1]
        arr[x-1] = arr[x]
        arr[x] = temp
        x -= 1
        result += 1
        

for i in range(ord('A'),ord('A')+n):
    curr = arr.index(chr(i))

    if i-ord('A') < curr: # 왼쪽으로 이동
        move2(i-ord('A') ,curr)
    if i-ord('A') > curr: # 오른쪽으로 이동
        move1(i-ord('A') ,curr)
    
#print(arr)
print(result)