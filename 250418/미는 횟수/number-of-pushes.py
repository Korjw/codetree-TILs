a = str(input())
b = str(input())
tf = True
for i in range(1,len(a)):
    a = a[-1] + a[:-1]
    #print(a)
    if a == b:
        print(i)
        tf = False
        break
if tf:
    print(-1)