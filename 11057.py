N = int(input())
dp = [[0 for _  in range(19)] for _ in range(1009)]

dp[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = sum(dp[i-1]) % 10007
        else:
            dp[i][j] = dp[i][j-1] - dp[i-1][j-1]

print(sum(dp[N])%10007)