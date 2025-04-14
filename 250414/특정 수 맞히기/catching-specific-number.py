a = -1
while a != 25:
    a = int(input())
    if a > 25:
        print('Lower')
    elif a < 25:
        print('Higher')
    else:
        print('Good')