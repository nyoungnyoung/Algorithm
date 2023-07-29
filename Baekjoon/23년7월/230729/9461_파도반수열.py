import sys
input = sys.stdin.readline

T = int(input().strip())
# dp 선언 + dp의 길이보다 N이 크거나 같으면 dp에 추가해주기
dp = [0, 1, 1, 1, 2, 2]
for _ in range(T):
    N = int(input().strip())
    if N >= len(dp):
        for i in range(len(dp), N + 1):
            # 점화식 dp[i] = dp[i-1] + dp[i-5]
            dp.append(dp[i - 1] + dp[i - 5])
    print(dp[N])
