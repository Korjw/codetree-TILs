s = str(input())
for i in range(len(s)-1,-1,-1):
    if i % 2 == 1:
        print(s[i],end ='')