a1,a2 = map(str,input().split())
b1,b2 = map(str,input().split())
if (int(a1) >= 19 and a2 == 'M') or (int(b1) >= 19 and b2 == 'M'):
    print(1)
else:
    print(0)