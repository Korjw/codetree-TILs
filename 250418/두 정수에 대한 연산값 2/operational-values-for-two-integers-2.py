a, b = map(int, input().split())

def func(a,b):
    if a < b:
        a += 10
        b *= 2
    else:
        b += 10
        a *= 2
    return a,b

a, b = func(a,b)
print(a,b)
# Please write your code here.