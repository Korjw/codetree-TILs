n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

for a1,a2 in queries:
    cnt = 0
    for i in range(a1-1,a2):
        cnt += arr[i]
    print(cnt)
# Please write your code here.