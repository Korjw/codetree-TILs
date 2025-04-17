f = True
for _ in range(5):
    a = int(input())
    if a % 3 != 0:
        f = False
if f:
    print(1)
else:
    print(0)