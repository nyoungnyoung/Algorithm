N = int(input())

dp = [0 for _ in range(N+1)]
dp[1] = 1

# N = 1 : 1개 / N = 2 : 1 개 / N = 3 : 2개 / N = 4 : 3개 / N = 5 : 5개
# dp[i] = dp[i - 2] + dp[i - 1]
for i in range(2, N + 1):
    dp[i] = dp[i - 2] + dp[i - 1]

print(dp[N])