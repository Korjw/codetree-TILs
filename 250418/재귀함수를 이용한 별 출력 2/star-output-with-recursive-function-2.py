n = int(input())

def draw(n):
    if n == 0:
        return
    for _ in range(n):
        print('*',end = ' ')
    print()
    draw(n-1)

def draw2(x):
    if x == n+1:
        return
    for _ in range(x):
        print('*',end = ' ')
    print()
    draw2(x+1)
draw(n)
draw2(1)
# Please write your code here.