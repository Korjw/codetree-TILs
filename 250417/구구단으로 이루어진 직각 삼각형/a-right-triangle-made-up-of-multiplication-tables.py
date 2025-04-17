n = int(input())
cnt = 0
for i in range(n,0,-1):
    cnt += 1
    for j in range(1,i+1):
        if j != 1:
            print('/',end = ' ')
        print(cnt,'*',j,'=',cnt*j,end = ' ')
    print()