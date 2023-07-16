N = int(input())
dp = [0 for _ in range(N + 1)]
if N <= 3: print(N)     # 1 / 2 / 3
else:
    dp[1], dp[2] = 1, 2
    # 3 ~ N까지 점화식으로 dp 채워주기
    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp[i] % 10007)