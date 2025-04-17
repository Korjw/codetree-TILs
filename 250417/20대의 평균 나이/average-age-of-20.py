cnt, n = 0, 0
while True:
    a = int(input())
    if a < 20 or a >= 30:
        break
    else:
        cnt += 1
        n += a
print('{:.2f}'.format(round(n/cnt,2)))