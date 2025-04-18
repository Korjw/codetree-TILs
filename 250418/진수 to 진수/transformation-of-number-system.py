a, b = map(int, input().split())
n = input()
n = str(n)
cnt = 0
result = 0
for i in range(len(n)-1,-1,-1):
    result += (a ** cnt) * int(n[i])
    cnt+=1
#print(result)
string = ""
while result >= b:
    string = str(result % b) + string
    result //= b
print(str(result % b) + string)


# Please write your code here.