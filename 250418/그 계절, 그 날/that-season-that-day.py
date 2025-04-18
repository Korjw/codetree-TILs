Y, M, D = map(int, input().split())

tf = False
if Y % 4 == 0:
    tf = True
    if Y % 100 == 0:
        tf = False
        if Y % 400 == 0:
            tf = True
if not tf and M == 2 and D > 28:
    print(-1)
elif M in ([2,4,6,9,11]) and D == 31:
    print(-1)
else:
    if M >= 3 and M <= 5:
        print('Spring')
    elif M >= 6 and M <= 8:
        print('Summer')
    elif M >= 9 and M <= 11:
        print('Fall')
    else:
        print('Winter')
# Please write your code here.