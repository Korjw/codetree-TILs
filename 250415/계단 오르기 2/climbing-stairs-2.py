n = int(input())
coin = [0] + list(map(int, input().split()))

dp = [[0 for _ in range(4)] for __ in range(n+1)] # i번째 서있음, j번 1계단 갔음
dp[0][0] = 0
dp[1][1] = coin[1]
dp[2][0] = coin[2]

for i in range(2,n+1):
    for j in range(1,4):
        if i == 0:
            dp[i][j] = 0
        dp[i][j] = max(dp[i-1][j-1] + coin[i], dp[i-2][j] + coin[i])

# for i in range(n+1):
#     for j in range(4):
#         #print(dp[i][j], end = ' ')
#     #print()
print(max(dp[n]))